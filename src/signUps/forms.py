from django import forms
from.models import signUp

from django.contrib.auth.models import User

#BOTH OF THESE NOT REQUIRED , REMOVE WHEN YOU REMOVE MODELS
class SignUpForm(forms.ModelForm):
	class Meta:
		model = signUp

class LoginForm(forms.ModelForm):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
			
