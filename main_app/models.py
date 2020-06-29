from django.db import models
from django.urls import reverse

# Create your models here.

class Artist(models.Model):
  name = models.CharField(max_length=100)

class Venue(models.Model):
  name = models.CharField(max_length=100)
  location = models.CharField(max_length=100)

  def get_absolute_url(self):
    return reverse('detail', kwargs={'venue_id': self.id})

class Concert(models.Model):
  artists = models.ManyToManyField(Artist)
  venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
  date = models.DateField()
  best_songs = models.TextField(max_length=250)

  class Meta:
    ordering = ['-date']
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'concert_id': self.id})
   