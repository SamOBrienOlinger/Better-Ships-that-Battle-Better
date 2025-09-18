"""Core views for Better Ships That Battle Better project.

This module contains views for user authentication, profile management and 
game-related functionality.
"""

import json

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Avg
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt

from pirates.forms import UserProfileForm
from pirates.models import Game, PirateQueen, UserProfile


# Authentication Views
def register_view(request):
    """User registration"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request,
                f'Account created for {username}! Please create your pirate profile.'
            )
            login(request, user)
            return redirect('profile_create')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def login_view(request):
    """Custom login view"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'registration/login.html')


def logout_view(request):
    """User logout"""
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')


@login_required
def profile_create(request):
    """Create user profile"""
    if hasattr(request.user, 'userprofile'):
        return redirect('profile_edit')

    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, f'Welcome aboard, Captain {profile.pirate_name}!')
            return redirect('dashboard')
    else:
        form = UserProfileForm()

    pirate_queens = PirateQueen.objects.all()
    return render(request, 'pirates/profile_create.html', {
        'form': form,
        'pirate_queens': pirate_queens
    })


@login_required
def profile_edit(request):
    """Edit user profile"""
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('dashboard')
    else:
        form = UserProfileForm(instance=profile)

    pirate_queens = PirateQueen.objects.all()
    return render(request, 'pirates/profile_edit.html', {
        'form': form,
        'profile': profile,
        'pirate_queens': pirate_queens
    })


@login_required
def dashboard(request):
    """User dashboard with stats and recent games"""
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        return redirect('profile_create')

    games = Game.objects.filter(player=profile)
    recent_games = games.order_by('-played_at')[:5]

    # Calculate stats
    total_games = games.count()
    wins = games.filter(result='win').count()
    losses = games.filter(result='loss').count()
    win_rate = round((wins / total_games * 100) if total_games > 0 else 0)
    avg_shots = games.aggregate(avg=Avg('shots_fired'))['avg']
    avg_shots = round(avg_shots) if avg_shots else 0
    total_ships_sunk = sum(game.ships_sunk for game in games)

    stats = {
        'total_games': total_games,
        'wins': wins,
        'losses': losses,
        'win_rate': win_rate,
        'avg_shots': avg_shots,
        'total_ships_sunk': total_ships_sunk
    }

    return render(request, 'pirates/dashboard.html', {
        'profile': profile,
        'recent_games': recent_games,
        'stats': stats
    })


@login_required
def game_history(request):
    """Full game history"""
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        return redirect('profile_create')

    games = Game.objects.filter(player=profile).order_by('-played_at')

    # Calculate stats
    total_games = games.count()
    wins = games.filter(result='win').count()
    losses = games.filter(result='loss').count()
    win_rate = round((wins / total_games * 100) if total_games > 0 else 0)

    stats = {
        'total_games': total_games,
        'wins': wins,
        'losses': losses,
        'win_rate': win_rate
    }

    return render(request, 'pirates/game_history.html', {
        'profile': profile,
        'games': games,
        'stats': stats
    })


@csrf_exempt
@login_required
def save_game_result(request):
    """Save game result via AJAX"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            profile = UserProfile.objects.get(user=request.user)

            Game.objects.create(
                player=profile,
                result=data.get('result'),
                shots_fired=data.get('shots_fired'),
                ships_sunk=data.get('ships_sunk'),
                difficulty=profile.preferred_difficulty,
                duration_seconds=data.get('duration_seconds')
            )

            return JsonResponse({'success': True})
        except (json.JSONDecodeError, UserProfile.DoesNotExist, ValueError) as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})


def home(request):
    """
    Serve the battleship game homepage with authentication
    """
    profile = None
    stats = None

    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            games = Game.objects.filter(player=profile)
            total_games = games.count()
            wins = games.filter(result='win').count()
            losses = games.filter(result='loss').count()
            win_rate = round((wins / total_games * 100) if total_games > 0 else 0)

            stats = {
                'total_games': total_games,
                'wins': wins,
                'losses': losses,
                'win_rate': win_rate
            }
        except UserProfile.DoesNotExist:
            pass

    context = {
        'profile': profile,
        'stats': stats
    }
    return render(request, 'home.html', context)


def game(request):
    """
    Main game interface for both authenticated and guest users
    """
    profile = None
    shots_available = 15  # Default for guests

    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            # Get shots based on difficulty
            shots_map = {'easy': 20, 'normal': 15, 'hard': 10}
            shots_available = shots_map.get(profile.preferred_difficulty, 15)
        except UserProfile.DoesNotExist:
            pass

    context = {
        'profile': profile,
        'shots_available': shots_available
    }
    return render(request, 'game.html', context)


def terminal_game(request):
    """
    Serve a simple terminal-style interface for the command line game
    """
    return render(request, 'terminal.html')
