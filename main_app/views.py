from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Venue, Concert, Artist
from .forms import ConcertForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def venues_index(request):
  venues = Venue.objects.all()
  return render(request, 'venues/index.html', { 'venues': venues })

def venues_detail(request, venue_id):
  venue = Venue.objects.get(id=venue_id)
  return render(request, 'venues/detail.html', { 'venue': venue })

def new_concert(request, venue_id):
  venue_id = venue_id
  concert_form = ConcertForm()
  artists = Artist.objects.all()
  if request.method == 'POST':
    concert_artists = request.POST.getlist('artists')
    for i in range(0, len(concert_artists)):
        concert_artists[i] = int(concert_artists[i])
    venue = Venue.objects.get(id=venue_id)
    form = Concert.objects.create(venue=venue, date=request.POST['date'], best_songs=request.POST['best_songs'])
    form.artists.set(concert_artists)
    new_concert = form.save()
    return redirect('concert_detail', concert_id=form.id)
  return render(request, 'concerts/new.html', { 'artists': artists, 'venue_id': venue_id, 'concert_form': concert_form })

def concerts_detail(request, concert_id):
  concert = Concert.objects.get(id=concert_id)
  concert_form = ConcertForm()
  artists = concert.artists.all()
  venue = concert.venue
  print(artists)
  return render(request, 'concerts/detail.html', { 'concert': concert, 'concert_form': concert_form, 'artists': artists, 'venue': venue })

class VenueCreate(CreateView):
  model = Venue
  fields = '__all__'

class VenueUpdate(UpdateView):
  model = Venue
  fields = '__all__'

class VenueDelete(DeleteView):
  model = Venue
  success_url = '/venues/'

def artists_index(request):
  artists = Artist.objects.all()
  return render(request, 'artists/index.html', { 'artists': artists })

class ArtistCreate(CreateView):
  model = Artist
  fields = '__all__'
  success_url = '/artists/'

class ArtistDelete(DeleteView):
  model = Artist
  success_url = '/artists/'

def unassoc_artist(request, concert_id, artist_id):
  Concert.objects.get(id=concert_id).artists.remove(artist_id)
  return redirect('concert_detail', concert_id=concert_id)

