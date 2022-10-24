from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill, Thumbnail
from django.conf import settings

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = ProcessedImageField(
        upload_to = 'images/',
        blank = True,
        processors=[ResizeToFill(500, 500)],
        format='JPEG',
        options={'quality' : 100},
    )
    Thumbnail = ImageSpecField(
        source='image',
        processors=[Thumbnail(300, 300)],
        format='JPEG',
        options={'quality' : 100},
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)