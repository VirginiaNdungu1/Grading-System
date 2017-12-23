from django import forms
from .models import Profile, User, Project
from datetime import datetime as dt


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_pic',)


class CreateProjectForm(forms.ModelForm):
    due_date = forms.DateField(label='Project Date', input_formats=[
        '%d/%m/%Y'])
    due_time = forms.TimeField(
        label='Due TIme', widget=forms.TimeInput(format='%H:%M'))

    class Meta:
        model = Project
        exclude = ['lec', 'submissions']
