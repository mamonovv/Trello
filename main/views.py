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


def main_page(request):
  boards = Board.objects.all()
  return render(request, 'main/main.html', {'boards': boards,})


def new_board(request):
  if request.method == 'POST':
    form = AddBoardForm(request.POST)
    if form.is_valid():
      board = form.save(commit=False)
      board.user = request.user
      board.save()
      return redirect('main')
  else:
    form = AddBoardForm()

  context = {
    'form': form, 
    'cardBtn': 'Создать доску'
  }
  # return render(request, 'main/newBoard.html', context=context)
  return render(request, 'main/newBoard.html', context=context)

def show_board(request, board_id):
  return HttpResponse(f"Доска - {board_id}")