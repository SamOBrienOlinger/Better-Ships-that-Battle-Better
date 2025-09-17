"""Forms for Pirate profiles (create/edit)."""
from django import forms
from .models import UserProfile, PirateQueen

class UserProfileForm(forms.ModelForm):
    """ModelForm to create or edit a user's pirate profile."""
    class Meta:
        model = UserProfile
        fields = ['pirate_name', 'chosen_pirate_queen', 'bio', 'preferred_difficulty']
        widgets = {
            'pirate_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your pirate captain name'
            }),
            'chosen_pirate_queen': forms.Select(attrs={
                'class': 'form-control'
            }),
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Tell your tale of the high seas...'
            }),
            'preferred_difficulty': forms.Select(attrs={
                'class': 'form-control'
            })
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Use the model's default manager to satisfy static analyzers
        self.fields['chosen_pirate_queen'].queryset = PirateQueen._meta.default_manager.all()
        self.fields['chosen_pirate_queen'].empty_label = "Choose your Pirate Queen..."
