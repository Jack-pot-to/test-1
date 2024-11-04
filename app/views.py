from django.shortcuts import render
from django.views.generic import TemplateView

class HomepageView(TemplateView):
    template_name = 'app/home.html'

class AboutpageView(TemplateView):
    template_name = 'app/about.html'
