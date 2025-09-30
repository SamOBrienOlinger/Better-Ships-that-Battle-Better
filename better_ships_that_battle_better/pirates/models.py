from typing import TYPE_CHECKING
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

if TYPE_CHECKING:
    from django.db.models.manager import RelatedManager
    from django.db.models.query import QuerySet

class PirateQueen(models.Model):
    """Historical Pirate Queens for user avatars"""
    name = models.CharField(max_length=100)
    description = models.TextField()
    historical_period = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    image_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
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
    
    # Type hints for Django reverse relations
    if TYPE_CHECKING:
        game_set: 'RelatedManager[Game]'
    
    # Game preferences
    preferred_difficulty = models.CharField(
        max_length=20,
        choices=[
            ('easy', 'Easy (25 shots)'),
            ('normal', 'Normal (20 shots)'),
            ('hard', 'Hard (15 shots)'),
        ],
        default='normal'
    )
    
    def __str__(self) -> str:
        # Django provides access to related model fields
        return f"Captain {self.pirate_name} ({self.user.username})"  # type: ignore[attr-defined]
    
    @property
    def total_games(self) -> int:
        # Django automatically creates reverse relationship managers
        return self.game_set.count()  # type: ignore[attr-defined]
    
    @property
    def wins(self) -> int:
        return self.game_set.filter(result='win').count()  # type: ignore[attr-defined]
    
    @property
    def losses(self) -> int:
        return self.game_set.filter(result='loss').count()  # type: ignore[attr-defined]
    
    @property
    def win_percentage(self) -> float:
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
    
    def __str__(self) -> str:
        # Django provides get_*_display methods for choice fields and related field access
        return f"{self.player.pirate_name} - {self.get_result_display()} ({self.played_at.strftime('%Y-%m-%d')})"  # type: ignore[attr-defined]
    
    class Meta:
        ordering = ['-played_at']
