from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm


from .models import *


class AddBoardForm(forms.ModelForm):
  class Meta:
    model = Boards
    fields = '__all__'


class AddColumnForm(forms.ModelForm):
  class Meta:
    model = Card
    fields = '__all__'


class AddCardForm(forms.ModelForm):
  class Meta:
    model = Card
    fields = '__all__'


class RegisterUserForm(UserCreationForm):
  username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-form', 'placeholder': "Имя пользователя"}))
  password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-form', 'placeholder': "Пароль"}))
  password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-form', 'placeholder': "Введите пароль еще раз"}))


  class Meta:
    model = User
    fields = ['username', 'password1', 'password2']


class LoginUserForm(AuthenticationForm):
  username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-form', 'placeholder': "Имя пользователя"}))
  password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-form', 'placeholder': "Пароль"}))
