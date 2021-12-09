from django.shortcuts import render
from .models import *


def index(request):
  return render(request, 'main/index.html')


def login(request):
  context = {
    'titlePage': 'Авторизация',
    'titleCard': 'Войти в трелло',
    'cardBtn': 'Войти',
    'anotherLink': 'Регистрация',
  }
  return render(request, 'main/reg-log.html', context=context)


def register(request):
  context = {
    'titlePage': 'Регистрация',
    'titleCard': 'Зарегистрироваться в трелло',
    'cardBtn': 'Зарегистрироваться',
    'anotherLink': 'Авторизация',
  }
  return render(request, 'main/reg-log.html', context=context)

