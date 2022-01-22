from django.shortcuts import render
from django.views import *
from .forms import *
from django.views.generic import *
from django.urls import reverse,reverse_lazy
from rest_framework import viewsets
from .serializers import *

# Create your views here.
class index(ListView):
    template_name='index.html'
    model=Books

class insert(CreateView):
    template_name='insert.html'
    form_class=BooksForm
    success_url=reverse_lazy('index')

class edit(UpdateView):
    template_name='edit.html'
    model=Books
    form_class=BooksForm
    success_url=reverse_lazy('index')

class delete(DeleteView):
    template_name='delete.html'
    model=Books
    success_url=reverse_lazy('index')

class BooksViewset(viewsets.ModelViewSet):
    serializer_class=BooksSerialzers
    queryset=Books.objects.all()