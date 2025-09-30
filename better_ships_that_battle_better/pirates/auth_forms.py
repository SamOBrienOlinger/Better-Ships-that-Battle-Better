"""Custom authentication forms for the Pirates app."""
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
import re


class CustomUserCreationForm(forms.Form):
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

    def clean_password1(self):
        """Validate password1."""
        password1 = self.cleaned_data.get('password1')
        if password1 and len(password1) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        return password1

    def clean_password2(self):
        """Validate that the two password entries match."""
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("The two password fields didn't match.")
        return password2

    def save(self, commit=True):
        """Save the user with the custom username validation."""
        user = User.objects.create_user(
            username=self.cleaned_data["username"],
            email=self.cleaned_data.get("email", ""),
            password=self.cleaned_data["password1"]
        )
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