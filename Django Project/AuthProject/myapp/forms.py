from django import forms
from .models import userSignup

class usersignupForm(forms.ModelForm):
    class Meta:
        model=userSignup
        fields='__all__'
