from django import forms
from django.contrib.auth.models import User
from registration.models import UserProfileInfo

class UserForm(forms.ModelForm):
    """Form definition for User."""
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        """Meta definition for Userform."""

        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    """Form definition for UserProfileInfo."""

    class Meta:
        """Meta definition for UserProfileInfoform."""

        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')

