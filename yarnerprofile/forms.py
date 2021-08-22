from django import forms

from .models import YarnerProfile

class YarnerProfileForm(forms.ModelForm):
    class Meta:
        model= YarnerProfile
        fields= ('avatar',)