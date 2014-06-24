from django import forms
from.models import signUp

class SignUpForm(forms.ModelForm):
	class Meta:
		model = signUp
		
