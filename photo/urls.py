from django.conf.urls import patterns, include, url
from .views import PhotoDetail, PhotoList

urlpatterns = patterns('',
    url(r'^$', PhotoList.as_view(), name='photo_list'),
    url(r'^(?P<pk>\d+)/$', PhotoDetail.as_view(), name='photo_detail'),
)