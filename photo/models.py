from django.db import models
from django.utils import timezone


class Photo(models.Model):
    title = models.CharField("Название", max_length=100)
    published = models.DateTimeField("Дата загрузки", default=timezone.now)
    desc = models.CharField("Описание", max_length=255)
    filepath = models.ImageField("Место хранения", upload_to='photos/%Y/%m')

    def __str__(self):
        return self.title
