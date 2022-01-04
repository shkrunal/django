from django import forms
from .models import Member

class memberform(forms.ModelForm):
    class Meta:
        model= Member
        fields=['username','email','phone','password']