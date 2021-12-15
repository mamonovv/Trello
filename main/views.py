from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.http import HttpResponse


from .forms import *
from .models import *
from .utils import *


pages = [
  'url'
]

def index(request):
  return render(request, 'main/index.html')


# def login(request):
#   context = {
#     'titlePage': 'Авторизация',
#     'titleCard': 'Войти в трелло',
#     'cardBtn': 'Войти',
#     'anotherLink': 'Регистрация',
#     'url_anotherLink': 'register',
#   }
#   return render(request, 'main/reg-log.html', context=context)

# def register(request):
#   if request.method == 'POST':
#     form = RegisterUserForm(request.POST)
#     if form.is_valid():
#       form.save()
#       return redirect('login')
#   else:
#     form = RegisterUserForm()

#   context = {
#     'titlePage': 'Регистрация',
#     'titleCard': 'Зарегистрироваться в трелло',
#     'cardBtn': 'Зарегистрироваться',
#     'anotherLink': 'Авторизация',
#     'url_anotherLink': 'login',
#     'form': form
#   }

#   return render(request, 'main/register.html', context=context)


class RegisterUser(CreateView):
  form_class = RegisterUserForm
  template_name = 'main/register.html'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      

      context['titlePage'] = 'Авторизация'
      context['titleCard'] = 'Зарегистрироваться в трелло'
      context['cardBtn'] = 'Зарегистрироваться'
      context['anotherLink'] = 'Авторизация'
      context['url_anotherLink'] = 'login'

      return dict(list(context.items()))

  def form_valid(self, form):
    user = form.save()
    login(self.request, user)
    return redirect('main')
  


class LoginUser(LoginView):
  form_class = LoginUserForm
  template_name = 'main/login.html'

  def get_context_data(self, *, object_list = None, **kwargs):
    context = super().get_context_data(**kwargs)

    context["titlePage"] = 'Авторизация'
    context["titleCard"] = 'Войти в трелло'
    context["cardBtn"] = 'Авторизироваться'
    context["anotherLink"] = 'Регистрация'
    context["url_anotherLink"] = 'register'

    return dict(list(context.items()))


  def get_success_url(self):
    return reverse_lazy('main')



def logout_user(request):
  logout(request)
  return redirect('login')


def main_user(request, user_id):
  return HttpResponse(f"Отображение пользователя с id = {user_id}")

def main_page(request):
  return render(request, 'main/main.html')