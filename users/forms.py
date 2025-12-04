from django.forms import ModelForm
from django import forms
from . import models

class ProfileForm(ModelForm):
    class Meta:
        model = models.Profile
        fields = ['image', 'displayname', 'info']
        widgets = {
            'image': forms.FileInput(),
            'displayname': forms.TextInput(attrs={'placeholder': 'Add display name'}),
            'info': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add information'})
        }
