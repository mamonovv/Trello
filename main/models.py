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
  
  def get_absolute_url(self):
      return reverse('del_column', kwargs={'column_id': self.pk , 'board_id': self.board.pk}) #ВОТ ТУТ ПЫТАЛСЯ МЕНЯТЬ

class Card(models.Model):
  name = models.CharField(max_length = 255, verbose_name="Название карточки")
  content = models.TextField(verbose_name="Контент", null=True, blank=True)
  deadline = models.DateField(verbose_name="Срок выполнения", null=True, blank=True)
  photo = models.ImageField(upload_to = "photos/", verbose_name="Фото", null=True, blank=True)
  column = models.ForeignKey(Column, on_delete=models.CASCADE, editable=False, verbose_name="В какой колонке")


  def __str__(self):
      return self.name

  class Meta:
    verbose_name = 'Карточки'
    verbose_name_plural = 'Карточки'

  

