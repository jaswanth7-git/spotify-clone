from django.db import models

# Create your models here.
class Album(models.Model):
    artist=models.CharField(max_length=50)
    Album_Title=models.CharField(max_length=50)
    genre=models.CharField(max_length=10)
    album_logo=models.CharField(max_length=1000)
    casting=models.CharField(max_length=50, default='a')


    def __str__(self):
        return self.Album_Title+'-'+self.artist


    
class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)  
    file_type=models.CharField(max_length=10)
    song_title=models.CharField(max_length=250)
    song_play=models.FileField(upload_to='songs')
    def __str__(self):
        return self.song_title+'-'+self.file_type

