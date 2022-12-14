from django.db import models

# Create your models here.

class Review(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    movie_name = models.CharField(max_length=50)
    grade = models.IntegerField()
    creatd_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)