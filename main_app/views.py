from django.shortcuts import render
from .models import Concert

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def concerts_index(request):
  concerts = Concert.objects.all()
  return render(request, 'concerts/index.html', { 'concerts': concerts })