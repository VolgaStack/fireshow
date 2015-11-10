from django.views.generic import ListView, DetailView
from .models import *


class PhotoDetail(DetailView):
    model = Photo


class PhotoList(ListView):
    model = Photo
    paginate_by = 50
