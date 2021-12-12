from django.db import models

class Boards(models.Model):
  name = models.CharField(max_length = 255, verbose_name="Название доски")
  # user_id = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

  def __str__(self):
      return self.name

  class Meta:
    verbose_name = 'Доски'
    verbose_name_plural = 'Доски'
  


class Column(models.Model):
  name = models.CharField(max_length = 255, verbose_name="Название Колонки")
  board = models.ForeignKey(Boards, on_delete=models.CASCADE, null=True, verbose_name="Название доски")

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
  column = models.ForeignKey(Column, on_delete=models.CASCADE, verbose_name="Название колонки")
  board = models.ForeignKey(Boards, on_delete=models.CASCADE, null=True, verbose_name="Название доски")

  def __str__(self):
      return self.name

  class Meta:
    verbose_name = 'Карточки'
    verbose_name_plural = 'Карточки'

  

