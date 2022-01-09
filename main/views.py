from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.http import HttpResponse, JsonResponse


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
      return redirect('board', board.pk)
  else:
    form = AddBoardForm()

  context = {
    'form': form, 
    'cardBtn': 'Создать доску'
  }
  # return render(request, 'main/newBoard.html', context=context)
  return render(request, 'main/newBoard.html', context=context)

def is_ajax(request):
  return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def show_board(request, board_id):
  if is_ajax(request=request) and request.method == "GET":
    data = {
      'first': '1',
    }
    return JsonResponse(data)
  else:
    board = Board.objects.get(pk=board_id)
    return render(request, 'main/board.html', {'board': board})
  
  
def add_column():
  return HttpResponse('This is add_column')
def del_column():
  return HttpResponse('This is del_column')
def add_card():
  return HttpResponse('This is add_card')
def del_card():
  return HttpResponse('This is del_card')
def move_card():
  return HttpResponse('This is move_card')
def edit_card():
  return HttpResponse('This is edit_card')