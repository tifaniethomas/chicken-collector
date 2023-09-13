from typing import Any
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Chicken
from .forms import FeedingForm


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def add_feeding(request, chicken_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.chicken_id = chicken_id
    new_feeding.save()
  return redirect('detail', pk=chicken_id)

# Create your class-based views here.
class ChickensIndex(ListView):
    model = Chicken
    template_name = 'chickens/index.html'
    context_object_name = 'chickens'

class ChickensDetail(DetailView):
    model = Chicken
    feeding_form = FeedingForm()
    template_name = 'chickens/detail.html'
    extra_context={'feeding_form': feeding_form}

class ChickensCreate(CreateView):
    model = Chicken
    fields = '__all__'
    success_url = '/chickens/{chicken_id}'

class ChickenUpdate(UpdateView):
  model = Chicken
  fields = ['breed', 'description', 'age']

class ChickenDelete(DeleteView):
  model = Chicken
  success_url = '/chickens'
