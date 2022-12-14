from django.conf import settings
from django.db import models
from django.forms import ImageField
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import Thumbnail, ResizeToFill

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = ProcessedImageField(
        upload_to = 'images/', blank=True,
        processors=[Thumbnail(500, 500)],
        format='JPEG',
        options={'quality': 100}
    )
    thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(120, 120)],
        format='JPEG'
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)