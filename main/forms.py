from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from .models import *
class AddBoardForm(forms.ModelForm):
  name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mmv-input', 'placeholder': "Название доски доски"}))
  class Meta:
    model = Board
    fields = ['name',]
  

class AddColumnForm(forms.ModelForm):
  name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Введите название ...", 'class': 'add__board-input', 'id': 'add__board-input'}))
  class Meta:
    model = Column
    fields = ['name',]


class AddCardForm(forms.ModelForm):
  name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Карточка ...", 'class': 'add__board-input cardInput'}))
  class Meta:
    model = Card
    fields = ['name',]

class PopUpForm(forms.ModelForm):
  name = forms.CharField(widget=forms.TextInput)
  content = forms.CharField(widget=forms.Textarea, required=False)
  deadline = forms.DateField(required=False, input_formats = ['%Y-%m-%d'])
  photo = forms.ImageField(required=False)
  class Meta:
    model = Card
    fields = ('name', 'content', 'deadline', 'photo',)

class RegisterUserForm(UserCreationForm):
  username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Имя пользователя"}))
  password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Пароль"}))
  password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Введите пароль еще раз"}))
  class Meta:
    model = User
    fields = ['username', 'password1', 'password2']


class LoginUserForm(AuthenticationForm):
  username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Имя пользователя"}))
  password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Пароль"}))
