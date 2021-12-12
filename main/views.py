from django.shortcuts import render
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *
from .utils import *


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


# def register(request):
#   context = {
#     'titlePage': 'Регистрация',
#     'titleCard': 'Зарегистрироваться в трелло',
#     'cardBtn': 'Зарегистрироваться',
#     'anotherLink': 'Авторизация',
#     'url_anotherLink': 'login',

#   }
#   return render(request, 'main/reg-log.html', context=context)

class RegisterUser(CreateView):
  form_class = RegisterUserForm
  template_name = 'main/register.html'
  success_url = reverse_lazy('login')

  def get_context_data(self, *, object_list = None, **kwargs):
    context = super().get_context_data(**kwargs)

    context['titlePage'] = 'Регистрация'
    context['titleCard'] = 'Войти в трелло'
    context['cardBtn'] = 'Зарегистрироваться'
    context['anotherLink'] = 'Регистрация'
    context['url_anotherLink'] = 'register'

  def get_success_url(self):
    return reverse_lazy('main')



# class LoginUser(LoginView):
#   form_class = AuthentificationForm
#   template_name = 'main/reg-log.html'

#   def get_context_data(self, *, object_list = None, **kwargs):
#     context = super().get_context_data(**kwargs)

#     context['titlePage'] = 'Авторизация'
#     context['titleCard'] = 'Зарегистрироваться в трелло'
#     context['cardBtn'] = 'Зарегистрироваться'
#     context['anotherLink'] = 'Авторизация'
#     context['url_anotherLink'] = 'login'

#     return dict(list(context.items()))
