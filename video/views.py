from django.views.generic import ListView, DetailView
from .models import *


class VideoDetail(DetailView):
    model = Video


class VideoList(ListView):
    model = Video
    paginate_by = 20
