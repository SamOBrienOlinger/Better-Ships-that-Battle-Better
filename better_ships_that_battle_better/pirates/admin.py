from django.contrib import admin
from .models import PirateQueen, UserProfile, Game

@admin.register(PirateQueen)
class PirateQueenAdmin(admin.ModelAdmin):
    list_display = ['name', 'historical_period', 'region', 'created_at']
    list_filter = ['historical_period', 'region']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['pirate_name', 'user', 'chosen_pirate_queen', 'preferred_difficulty', 'total_games', 'win_percentage']
    list_filter = ['preferred_difficulty', 'chosen_pirate_queen', 'created_at']
    search_fields = ['pirate_name', 'user__username', 'user__email']
    readonly_fields = ['created_at', 'updated_at', 'total_games', 'wins', 'losses', 'win_percentage']
    
    def total_games(self, obj):
        return obj.total_games
    total_games.short_description = 'Total Games'  # type: ignore[attr-defined]
    
    def win_percentage(self, obj):
        return f"{obj.win_percentage}%"
    win_percentage.short_description = 'Win Rate'  # type: ignore[attr-defined]

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['player', 'result', 'shots_fired', 'ships_sunk', 'difficulty', 'played_at']
    list_filter = ['result', 'difficulty', 'played_at']
    search_fields = ['player__pirate_name', 'player__user__username']
    readonly_fields = ['played_at']
    date_hierarchy = 'played_at'
