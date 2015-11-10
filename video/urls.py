from django.conf.urls import patterns, include, url
from .views import VideoDetail, VideoList

urlpatterns = patterns('',
    url(r'^$', VideoList.as_view(), name='video_list'),
    url(r'^(?P<pk>\d+)/$', VideoDetail.as_view(), name='video_detail'),
)