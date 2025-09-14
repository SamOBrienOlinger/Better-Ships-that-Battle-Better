from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class PirateQueen(models.Model):
    """Historical Pirate Queens for user avatars"""
    name = models.CharField(max_length=100)
    description = models.TextField()
    historical_period = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    image_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} ({self.historical_period})"
    
    class Meta:
        ordering = ['name']

class UserProfile(models.Model):
    """Extended user profile for pirate captains"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pirate_name = models.CharField(max_length=100, help_text="Your captain name")
    chosen_pirate_queen = models.ForeignKey(PirateQueen, on_delete=models.SET_NULL, null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True, help_text="Tell us about your pirate adventures")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Game preferences
    preferred_difficulty = models.CharField(
        max_length=20,
        choices=[
            ('easy', 'Easy (15 shots)'),
            ('normal', 'Normal (10 shots)'),
            ('hard', 'Hard (7 shots)'),
        ],
        default='normal'
    )
    
    def __str__(self):
        return f"Captain {self.pirate_name} ({self.user.username})"
    
    @property
    def total_games(self):
        return self.game_set.count()
    
    @property
    def wins(self):
        return self.game_set.filter(result='win').count()
    
    @property
    def losses(self):
        return self.game_set.filter(result='loss').count()
    
    @property
    def win_percentage(self):
        if self.total_games == 0:
            return 0
        return round((self.wins / self.total_games) * 100, 1)

class Game(models.Model):
    """Individual game records"""
    RESULT_CHOICES = [
        ('win', 'Victory'),
        ('loss', 'Defeat'),
    ]
    
    player = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    result = models.CharField(max_length=10, choices=RESULT_CHOICES)
    shots_fired = models.IntegerField()
    ships_sunk = models.IntegerField()
    total_ships = models.IntegerField(default=5)
    difficulty = models.CharField(max_length=20, default='normal')
    duration_seconds = models.IntegerField(null=True, blank=True)
    played_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.player.pirate_name} - {self.get_result_display()} ({self.played_at.strftime('%Y-%m-%d')})"
    
    class Meta:
        ordering = ['-played_at']
