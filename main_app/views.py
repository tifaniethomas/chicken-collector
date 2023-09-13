from typing import Any
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Chicken


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# Create your class-based views here.
class ChickensIndex(ListView):
    model = Chicken
    template_name = 'chickens/index.html'
    context_object_name = 'chickens'

class ChickensDetail(DetailView):
    model = Chicken
    template_name = 'chickens/detail.html'

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
