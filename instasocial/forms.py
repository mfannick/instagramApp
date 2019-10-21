from django import forms
from . import models

class PostImage(forms.ModelForm):
    class Meta:
        model=models.Image
        fields=['image','imageName','imageCaption']

class CreateProfile(forms.ModelForm):
    class Meta:
        model=models.Profile
        fields=['userBio','userPic']

