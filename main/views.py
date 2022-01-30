from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict


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
  return render(request, 'main/newBoard.html', context=context)

def show_board(request, board_id):
  formColumn = AddColumnForm()
  formCard = AddCardForm()

  board = Board.objects.get(pk=board_id)
  columns = Column.objects.all()
  cards = Card.objects.all()
  return render(request, 'main/board.html', {'board': board, 'formColumn': formColumn, 'formCard': formCard, 'columns': columns, 'cards':cards})
  
  
def add_column(request, board_id):
  if request.method == 'POST':
    form = AddColumnForm(request.POST)
    if form.is_valid():
      column = form.save(commit=False)
      column.board = Board.objects.get(pk=board_id)
      column.save()
  response = {
    'pk': column.pk,
  }
  return JsonResponse(response)


def del_column(request, board_id, column_id):
  Column.objects.filter(pk=column_id).delete()
  response = {
    'data': 'true',
  }
  return JsonResponse(response)


def add_card(request, board_id, column_id):
  
  if request.method == 'POST':
    
    form = AddCardForm(request.POST)
    if form.is_valid():
      card = form.save(commit=False)
      card.column = Column.objects.get(pk=column_id)
      card.save()
  response = {
    'pk': card.pk,
  }
  return JsonResponse(response)


def del_card(request, board_id, card_id):
  Card.objects.filter(pk=card_id).delete()
  response = {
    'data': 'true',
  }
  return JsonResponse(response)


def move_card(request, board_id, col_id, card_id):
  card = Card.objects.get(pk=card_id)
  col = Column.objects.get(pk=col_id)
  card.column = col
  # card.name = 'pomidor'
  card.save()

  response = {
    'newCol': card.name
    
  }

  return JsonResponse(response)


def popup_save(request, board_id, card_id):
  # response = {
  #   'name': request.POST,
  # }
  # return JsonResponse(response)
  
  props = ['name', 'content', 'deadline', 'photo']

  card = Card.objects.get(pk=card_id)
  form = PopUpForm(request.POST, request.FILES, instance=card, initial=model_to_dict(card))

  if form.is_valid():
    form.save()

  # if form.is_valid():
  #   if form.has_changed():
  #     changed = form.changed_data
  #     if 'name' in changed:
  #       card.name = form.cleaned_data['name']
  #     if 'content' in changed:
  #       card.content = form.cleaned_data['content']
  #     if 'deadline' in changed:
  #       card.deadline = form.cleaned_data['deadline']
  #     if 'photo' in changed:
  #       card.photo = form.instance
      
    # card.save()
  else:
    response = {'Errors': form.errors.as_text()}
    return JsonResponse(response)

  response = {
    'name': card.name,
  }
  return JsonResponse(response)

def get_card(request, board_id, card_id):
  card = Card.objects.get(pk=card_id)

  if card.photo:
    photo = card.photo.url
  else:
    photo = None

  response = {
    'name': card.name,
    'content': card.content,
    'deadline': card.deadline,
    'photo': photo,
  }

  return JsonResponse(response)

def del_board(request, board_id):
  Board.objects.filter(pk=board_id).delete()
  response = {
    'data': 'true',
  }
  return JsonResponse(response)

