from django import forms
from lecturer.models import Profile, User


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_pic',)
