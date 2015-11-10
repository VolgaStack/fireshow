# -*- coding: utf-8 -*-

import datetime

from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField


class News(models.Model):
    title = models.CharField("Название", max_length=255)
    published = models.DateTimeField("Дата публикации")
    preview = RichTextUploadingField("Превью")
    content = RichTextUploadingField("Содержание")

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return timezone.now() > self.published >= timezone.now() - datetime.timedelta(days=1)