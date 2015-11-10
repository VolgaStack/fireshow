"""
Definition of urls for Fireshow.
"""

from django.conf.urls import patterns, include, url
from django.contrib import admin
from journal.views import ContactsPage, HomePage

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', HomePage.as_view(), name='home'),
    url(r'^photo/', include('photo.urls', namespace='photo')),
    url(r'^video/', include('video.urls', namespace='video')),
    url(r'^journal/', include('journal.urls', namespace='journal')),
    url(r'^contacts/$', ContactsPage.as_view(), name='contacts'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
)
