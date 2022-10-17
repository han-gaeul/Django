from django.db import models
from django.forms import ImageField
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import Thumbnail, ResizeToFill

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
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