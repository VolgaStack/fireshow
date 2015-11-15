from django.db import models
from django.utils import timezone


class Video(models.Model):
    title = models.CharField("Название", max_length=255)
    published = models.DateTimeField("Дата загрузки", default=timezone.now)
    thumbnail = models.ImageField("Превью", upload_to='video_thumbnails/')
    #filepath = models.FileField("Место хранения", upload_to='videos/%Y/%m/%d', blank=True)
    url = models.URLField("Ссылка на источник", blank=True)

    def __str__(self):
        return self.title
