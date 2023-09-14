from typing import Any
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Chicken, Toy
from .forms import FeedingForm


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def chickens_detail(request, chicken_id):
  chicken = Chicken.objects.get(id=chicken_id)
  id_list = chicken.toys.all().values_list('id')
  unassoc_toy = Toy.objects.exclude(id__in=id_list)
  # instantiate FeedingForm to be rendered in detail.html
  feeding_form = FeedingForm()
  return render(request, 'chickens/detail.html', {
    'chicken': chicken, 
    'feeding_form': feeding_form,
    'toys': unassoc_toy
  })

def add_feeding(request, chicken_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.chicken_id = chicken_id
    new_feeding.save()
  return redirect('detail', chicken_id)

def assoc_toy(request, chicken_id, toy_id):
  Chicken.objects.get(id=chicken_id).toys.add(toy_id)
  return redirect('detail', chicken_id=chicken_id)

def disassoc_toy(request, chicken_id, toy_id):
  Chicken.objects.get(id=chicken_id).toys.remove(toy_id)
  return redirect('detail', chicken_id=chicken_id)

# Create your class-based views here.
class ChickensIndex(ListView):
    model = Chicken
    template_name = 'chickens/index.html'
    context_object_name = 'chickens'

# class ChickensDetail(DetailView):
#     model = Chicken
#     feeding_form = FeedingForm()
#     template_name = 'chickens/detail.html'
#     extra_context={'feeding_form': feeding_form}

#     def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        id_list = self.toys.all().values_list('id')
#        context['unassoc_toys'] = Toy.objects.exclude(id__in=id_list)
#        return context
    


class ChickensCreate(CreateView):
    model = Chicken
    fields = ['name', 'breed', 'description', 'age']
    success_url = '/chickens/{chicken_id}'

class ChickenUpdate(UpdateView):
  model = Chicken
  fields = ['breed', 'description', 'age']

class ChickenDelete(DeleteView):
  model = Chicken
  success_url = '/chickens'

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys'
