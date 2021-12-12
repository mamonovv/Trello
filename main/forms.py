from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

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
  class Meta:
    model = User
    fields = ('username', 'password1', 'password2')
    widjets = {
      'username': forms.TextInput(),
      'password1': forms.PasswordInput(),
      'password2': forms.PasswordInput(),
    }