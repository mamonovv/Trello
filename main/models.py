from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Board(models.Model):
  name = models.CharField(max_length = 255, verbose_name="Название доски")
  user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, null=True, blank=True, verbose_name="Владелец доски")

  def __str__(self):
      return self.name

  class Meta:
    verbose_name = 'Доски'
    verbose_name_plural = 'Доски'

  def get_absolute_url(self):
      return reverse('board', kwargs={'board_id': self.pk})
  
  


class Column(models.Model):
  name = models.CharField(max_length = 255, verbose_name="Название Колонки")
  board = models.ForeignKey(Board, on_delete=models.CASCADE, editable=False, null=True, blank=True, verbose_name="В какой доске")

  def __str__(self):
      return self.name

  class Meta:
    verbose_name = 'Колонки'
    verbose_name_plural = 'Колонки'
  

class Card(models.Model):
  name = models.CharField(max_length = 255, verbose_name="Название карточки")
  content = models.TextField(verbose_name="Контент")
  deadline = models.DateTimeField(verbose_name="Срок выполнения")
  photo = models.ImageField(upload_to = "photos/", verbose_name="Фото")
  column = models.ForeignKey(Column, on_delete=models.CASCADE, verbose_name="В какой колонке")


  def __str__(self):
      return self.name

  class Meta:
    verbose_name = 'Карточки'
    verbose_name_plural = 'Карточки'

  

