from django.shortcuts import render
from .models import *

pages = [
  'url'
]

def index(request):
  return render(request, 'main/index.html')


def login(request):
  context = {
    'titlePage': 'Авторизация',
    'titleCard': 'Войти в трелло',
    'cardBtn': 'Войти',
    'anotherLink': 'Регистрация',
    'url_anotherLink': 'register',
  }
  return render(request, 'main/reg-log.html', context=context)


def register(request):
  context = {
    'titlePage': 'Регистрация',
    'titleCard': 'Зарегистрироваться в трелло',
    'cardBtn': 'Зарегистрироваться',
    'anotherLink': 'Авторизация',
    'url_anotherLink': 'login',

  }
  return render(request, 'main/reg-log.html', context=context)

