from django.db import models

class Artist(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    age = models.IntegerField(default=1, null=False)
    country = models.CharField(max_length=30, null=False)
    picture = models.ImageField(upload_to='artist_images/')
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

class Album(models.Model):
    title = models.CharField(max_length=50, null=False)
    year = models.PositiveIntegerField(default=1, null=False)
    GENDER_TYPES = {
        ('B', 'Balada'),
        ('P', 'Pop'),
        ('R', 'Rock'),
        ('G', 'Reggaeton'),
        ('C', 'Clasico'),
        ('S', 'Salsa'),
        ('V', 'Vallenato'),
        
    }
    gender = models.CharField(max_length=30, choices=GENDER_TYPES, null=False)
    artist = models.ForeignKey(Artist, null=True, blank=True, on_delete=models.SET_NULL)
    picture = models.ImageField(upload_to='album_images/')
    
    def __str__(self) -> str:
        return self.title
    
    def get_type_display(self):
        return dict(self.GENDER_TYPES).get(self.gender, self.gender)