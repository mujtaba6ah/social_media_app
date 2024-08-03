from django import forms
from django.contrib.auth.models import User

# This class for login form for users:
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

#  New user registration form class:
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = {'username','email','first_name'}

    # check if password matches:
        def check_password(self):
            if self.cleaned_data['password'] != self.clean_data['password2']:
                raise forms.ValidationError('password do nt march')
            return self.cleaned_data['password2']
    
    
    