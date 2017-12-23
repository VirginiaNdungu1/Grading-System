from django import forms
from .models import Profile, User, Project


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_pic',)


class CreateProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['lec', 'category', 'submissions']
