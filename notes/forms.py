# notes/forms.py
from django import forms
from .models import Notes
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'content', 'pinned']

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']