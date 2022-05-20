from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Matricula(models.Model):
    nombre=models.TextField(max_length=50,blank=False)
    primerapellido=models.TextField(max_length=50,blank=False)
    segundoapellido=models.TextField(max_length=50,blank=False)

class Blog(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "blogs")
    title = models.CharField(max_length = 250)
    description = models.CharField(max_length = 500)
    showcaseImage = models.ImageField(upload_to = "Images/")
    dateTimeOfCreation = models.DateTimeField(auto_now = True)
    shareURL = models.URLField()
    likes = models.IntegerField()
    disLikes = models.IntegerField()
    bookmarks = models.IntegerField()

    def __str__(self):
        return self.title
