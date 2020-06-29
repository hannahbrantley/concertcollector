from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('venues/', views.venues_index, name='index'),
  path('venues/<int:venue_id>/', views.venues_detail, name='detail'),
  path('venues/create/', views.VenueCreate.as_view(), name='venues_create'),
  path('venues/<int:pk>/update/', views.VenueUpdate.as_view(), name='venues_update'),
  path('venues/<int:pk>/delete/', views.VenueDelete.as_view(), name='venues_delete'),
  path('venues/<int:venue_id>/new_concert/', views.new_concert, name='new_concert'),
  path('concerts/<int:concert_id>/', views.concerts_detail, name='concert_detail'),
  path('artists/', views.artists_index, name='artists_index'),
  path('artists/create/', views.ArtistCreate.as_view(), name='artist_create'),
  path('artists/<int:pk>/delete/', views.ArtistDelete.as_view(), name='artists_delete'),
  path('cats/<int:concert_id>/unassoc_artist/<int:artist_id>/', views.unassoc_artist, name='unassoc_artist')
]