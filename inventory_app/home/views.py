from django.shortcuts import render

# Create your views here.
def mainpage(request):
  context={}
  return render(request, 'home/home.html')

def cart(request):
  context={}
  return render(request, 'home/cart.html')

def checkout(request):
  context={}
  return render(request, 'home/checkout.html')