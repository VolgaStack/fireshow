"""
Definition of urls for journal app.
"""

from django.conf.urls import patterns, include, url
from .views import JournalDetail, JournalList

urlpatterns = patterns('',
    url(r'^$', JournalList.as_view(), name='news_list'),
    url(r'^(?P<pk>\d+)/$', JournalDetail.as_view(), name='news_detail'),
)
