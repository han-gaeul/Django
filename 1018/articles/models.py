from re import M
from django.db import models
from django.forms import ImageField
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import Thumbnail,ResizeToFill

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    image = ProcessedImageField(
        upload_to = 'images/', blacnk=True,
        processors=[Thumbnail(500, 500)],
        format='JPEG',
        options={'quality': 100}
    )
    Thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(120, 120)],
        format='JPEG'
    )

class Comment(models.Model):
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True),
    article = models.ForeignKey(Article, on_delete=models.CASCADE)