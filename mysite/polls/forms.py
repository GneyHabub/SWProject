from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)


class StaffLoginForm(forms.Form):
    email = forms.CharField(label="", help_text="", widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(label="", help_text="", widget=forms.PasswordInput({'placeholder': 'Password'}))


class StudentLoginForm(forms.Form):
    email = forms.CharField(label="", help_text="", widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(label="", help_text="", widget=forms.PasswordInput({'placeholder': 'Password'}))
    poll_id = forms.IntegerField(label="", help_text="", widget=forms.TextInput(attrs={'placeholder': 'Poll id'}))
