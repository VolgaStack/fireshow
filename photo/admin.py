# -*- coding: utf-8 -*-

from django.contrib.admin import AdminSite
from django.contrib import admin
from .models import Photo


class PhotoAdmin(admin.ModelAdmin):
    list_filter = ['title', 'filepath']
    search_fields = ['title']


admin.site.register(Photo, PhotoAdmin)
