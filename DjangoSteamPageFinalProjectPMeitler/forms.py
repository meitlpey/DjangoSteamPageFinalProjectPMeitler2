# forms.py (inside your Django app)
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    class CustomUserCreationForm(UserCreationForm):
        error_messages = {
            'password_mismatch': "The two password fields didn't match.",
            'password_too_short': "Password must be at least 8 characters.",
            'password_common': "Password is too common.",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize labels and other attributes if needed
        self.fields['username'].label = 'Username'
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Confirm Password'
