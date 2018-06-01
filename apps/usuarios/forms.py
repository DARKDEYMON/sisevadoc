from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class crear_user_form(UserCreationForm):
	#password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
	#password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
	#email = forms.EmailField(required=True)
	class Meta:
		model=User
		fields=[
			'username',
			#'password1',
			#'password2',
			'first_name',
			'last_name',
			'email'
		]