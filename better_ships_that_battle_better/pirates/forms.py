"""Forms for the Pirates app: profile create/edit."""
from django import forms
from .models import UserProfile, PirateQueen


class UserProfileForm(forms.ModelForm):
    """Form to create and edit a user's pirate profile."""

    class Meta:
        """Meta class for UserProfileForm."""
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
        """Initialize form and set pirate queen choices."""
        super().__init__(*args, **kwargs)
        # Django automatically provides objects manager for all models at runtime
        self.fields['chosen_pirate_queen'].queryset = PirateQueen.objects.all()  # type: ignore[attr-defined]
        self.fields['chosen_pirate_queen'].empty_label = "Choose your Pirate Queen..."  # type: ignore[attr-defined]
