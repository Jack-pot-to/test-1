from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import WorkOuts
from django.urls import reverse_lazy

class HomepageView(TemplateView):
    template_name = 'app/home.html'


class ServicespageView(TemplateView):
    template_name = 'app/services.html'


class AboutpageView(TemplateView):
    template_name = 'app/about.html'


class ContactpageView(TemplateView):
    template_name = 'app/contact.html'


class WorkOutsListView(ListView):
    model = WorkOuts
    context_object_name = 'WorkOut'
    template_name = 'app/workouts_list.html'


class WorkOutsDetailView(DetailView):
    model = WorkOuts
    context_object_name = 'WorkOuts'
    template_name = 'app/workouts_detail.html'


class WorkOutsCreateView(CreateView):
    model = WorkOuts
    fields = ['name', 'category', 'duration', 'calories_burned']
    template_name = 'app/workouts_create.html'

class WorkOutsUpdateView(UpdateView):
    model = WorkOuts
    fields = ['name', 'category', 'duration', 'calories_burned']
    template_name = 'app/workouts_update.html'

class WorkOutsDeleteView(DeleteView):
    model = WorkOuts
    template_name = 'app/workouts_delete.html'
    success_url = reverse_lazy('services')