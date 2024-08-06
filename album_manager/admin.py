from django.contrib import admin
from .models import Album
from .models import Artist
# Register your models here.
@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    pass

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    pass