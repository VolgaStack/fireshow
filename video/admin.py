# -*- coding: utf-8 -*-

from django.contrib.admin import AdminSite
from django.contrib import admin
from .models import Video


class VideoAdmin(admin.ModelAdmin):
    list_filter = ['title', 'url']
    search_fields = ['title']

admin.site.register(Video, VideoAdmin)
