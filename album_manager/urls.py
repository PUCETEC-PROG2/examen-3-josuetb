from django.urls import path

from . import views

app_name = "album_manager"
urlpatterns = [
    path("", views.index, name="index"),
    path("album/<int:album_id>/", views.album, name="album"),
    path("add_album/", views.add_album, name="add_album"),
    path("edit_album/<int:id>/", views.edit_album, name="edit_album"),
    path("delete_album/<int:id>/", views.delete_album, name="delete_album"),
    path("artists", views.artists, name="artists"),
    path("artist/<int:artist_id>/", views.artist, name="artist"),
    path("add_artist/", views.add_artist, name="add_artist"),
    path("edit_artist/<int:id>/", views.edit_artist, name="edit_artist"),
    path("delete_artist/<int:id>/", views.delete_artist, name="delete_artist")
]