from django.shortcuts import render
from django.shortcuts import get_object_or_404
# Create your views here.
from .models import Cart


def index(request, pk):
   main = get_object_or_404(Cart,pk)