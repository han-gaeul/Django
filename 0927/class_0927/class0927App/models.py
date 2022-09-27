from django.db import models

# Create your models here.
class articles(models.Model):
    content = models.TextField()