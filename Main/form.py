from django import forms

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from.models import Review
from django.contrib.auth.models import User
class RegestrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']


class LoginForm(AuthenticationForm):
    
    username=UsernameField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(label='Password',strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current_password','class':'form-control'}))

class Review_From(forms.ModelForm):
    
    class Meta:
        model=Review
        fields=('comment','rating')
        