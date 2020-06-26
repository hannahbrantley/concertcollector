from django.db import models

# Create your models here.

class Concert(models.Model):
  artist = models.CharField(max_length=100)
  venue = models.CharField(max_length=100)
  date = models.DateField()
  bestsongs = models.TextField(max_length=250)
  notes = models.TextField(max_length=250)

  def __str__(self):
    return self.artist 