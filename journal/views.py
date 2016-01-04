from django.shortcuts import render_to_response, redirect
from django.views.generic import ListView, DetailView, TemplateView
from .models import *
from photo.models import Photo
from video.models import Video

class HomePage(TemplateView):
    template_name = 'fireshow/main.html'

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        images = Photo.objects.all().order_by('-published')[:6]
        videos = Video.objects.all().order_by('-published')[:4]
        context['images'] = images
        context['videos'] = videos
        return context


class ContactsPage(TemplateView):
    template_name = 'fireshow/contacts.html'


class JournalDetail(DetailView):
    model = News


class JournalList(ListView):
    model = News
    paginate_by = 20