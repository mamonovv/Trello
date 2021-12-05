from django.shortcuts import render
from .models import *


def index(request):
  return render(request, 'main/index.html')


def login(request):
  return render(request, 'main/login.html')


# class RegisterUser(DataMixin, CreateView):
#   form_class = UserCreationForm
#   template_name = '/register.html'
#   success_url = reverse_lazy('login')

#   def get_context_data(self, *, object_list=None, **kwargs):
#       context = super().get_context_data(**kwargs)
#       c_def = self.get_user_context(title='Регистрация')
#       return dict(list(context.items()) + list(c_def.items()))
  