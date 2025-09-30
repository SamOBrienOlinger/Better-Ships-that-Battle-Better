"""Custom authentication forms for the Pirates app."""
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class CustomUserCreationForm(UserCreationForm):
    """Custom user creation form that allows any characters in username."""
    
    username = forms.CharField(
        max_length=150,
        help_text="Required. 150 characters or fewer. Any characters allowed.",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Choose your captain username'
        })
    )
    
    email = forms.EmailField(
        required=False,
        help_text="Optional. We'll use this for important fleet communications.",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'your.email@example.com (optional)'
        })
    )
    
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password'
        }),
        help_text="Your password must be at least 8 characters long."
    )
    
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm your password'
        }),
        help_text="Enter the same password as before, for verification."
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        
    def clean_username(self):
        """Custom username validation - allows any characters."""
        username = self.cleaned_data.get('username')
        
        if not username:
            raise ValidationError("Username is required.")
            
        if len(username.strip()) == 0:
            raise ValidationError("Username cannot be just whitespace.")
            
        if len(username) > 150:
            raise ValidationError("Username must be 150 characters or fewer.")
            
        # Check if username already exists (case-insensitive for better UX)
        if User.objects.filter(username__iexact=username).exists():
            raise ValidationError("A user with that username already exists.")
            
        return username

    def save(self, commit=True):
        """Save the user with the custom username validation."""
        user = super().save(commit=False)
        # Ensure username is saved exactly as entered
        user.username = self.cleaned_data["username"]
        if commit:
            user.save()
        return user


class CustomAuthenticationForm(AuthenticationForm):
    """Custom login form with better styling."""
    
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username',
            'autofocus': True
        })
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password'
        })
    )

    def clean_username(self):
        """Allow any characters in username for login."""
        return self.cleaned_data.get('username')