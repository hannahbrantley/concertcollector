from django.contrib import admin
from .models import Concert, Venue, Artist

# Register your models here.

admin.site.register(Concert)
admin.site.register(Venue)
admin.site.register(Artist)