from django.shortcuts import render_to_response, redirect
from django.views.generic import ListView, DetailView, TemplateView
from .models import *

class HomePage(TemplateView):
    template_name = 'fireshow/main.html'


class ContactsPage(TemplateView):
    template_name = 'fireshow/contacts.html'


class JournalDetail(DetailView):
    model = News


class JournalList(ListView):
    model = News
    paginate_by = 20