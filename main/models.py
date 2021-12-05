from django.db import models

class Boards(models.Model):
  name = models.CharField(max_length = 255)
  # user_id = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

  def __str__(self):
      return self.name
  


class Column(models.Model):
  name = models.CharField(max_length = 255)
  board_id = models.ForeignKey(Boards, on_delete=models.CASCADE)

  def __str__(self):
      return self.name
  

class Card(models.Model):
  name = models.CharField(max_length = 255)
  content = models.TextField()
  deadline = models.DateTimeField()
  photo = models.ImageField(upload_to = "photos/")
  column_id = models.ForeignKey(Column, on_delete=models.CASCADE)
  board_id = models.ForeignKey(Boards, on_delete=models.CASCADE)

  def __str__(self):
      return self.name
  

