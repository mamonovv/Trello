from django.shortcuts import render
from .models import *
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView


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
  success_url = reverse_lazy('login')

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      

      context['titlePage'] = 'Авторизация'
      context['titleCard'] = 'Зарегистрироваться в трелло'
      context['cardBtn'] = 'Зарегистрироваться'
      context['anotherLink'] = 'Авторизация'
      context['url_anotherLink'] = 'login'

      return dict(list(context.items()))
  


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
    return reverse_lazy('home')