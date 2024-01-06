from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *
# Create your views here.
def mainpage(request):
  if request.user.is_authenticated:
    member = request.user.member
    order, created = Order.objects.get_or_create(member=member)
    items = order.orderitem_set.all() 
    cartItems = order.get_cart_items
  else:
    items = []
    order = {'get_cart_items':0}
    cartItems = order['get_cart_items']

  components = Component.objects.all()
  context={'components':components, 'cartItems':cartItems}
  return render(request, 'home/home.html',context)

def cart(request): 
  if request.user.is_authenticated:
    member = request.user.member
    order, created = Order.objects.get_or_create(member=member)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items 
  else:
    items = []
    order = {'get_cart_items':0}
    cartItems = order['get_cart_items']

  #print(items) 
  context={'items':items,'order':order, 'cartItems':cartItems}
  return render(request, 'home/cart.html',context)

def checkout(request):
  if request.user.is_authenticated:
    member = request.user.member
    order, created = Order.objects.get_or_create(member=member)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items 
  else:
    items = []
    order = {'get_cart_items':0}
    cartItems = order['get_cart_items']

  #print(items) 
  context={'items':items,'order':order, 'cartItems':cartItems}
  return render(request, 'home/checkout.html',context)

def updateItem(request):
  data = json.loads(request.body)
  componentId = data['component_id']
  action = data['action'] 
  print('Action:', action)
  print('Component:', componentId)
  member = request.user.member
  component = Component.objects.get(id=componentId)
  order, created = Order.objects.get_or_create(member=member)
  orderItem, created = OrderItem.objects.get_or_create(order=order, component=component)
  if action == 'add':
    orderItem.quantity = (orderItem.quantity + 1)
  elif action == 'remove':
    orderItem.quantity = (orderItem.quantity - 1)
  orderItem.save()
  if orderItem.quantity <= 0:
    orderItem.delete()
  return JsonResponse ('Item was added', safe=False)

def processOrder(request):
  return JsonResponse ('order placed', safe=False)