from django.shortcuts import render
from .models import *
# Create your views here.
def mainpage(request):
  components = Component.objects.all()
  context={'components':components}
  return render(request, 'home/home.html',context)

def cart(request):
  context={}
  return render(request, 'home/cart.html')

def checkout(request):
  context={}
  return render(request, 'home/checkout.html')