from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *
# Create your views here.
def mainpage(request):
  if request.user.is_authenticated:
    member = request.user.member
    order, created = Order.objects.get_or_create(member=member,complete=False)
    items = order.orderitem_set.all() 
    cartItems = order.get_cart_items
  else:
    items = []
    order = {'get_cart_items':0}
    cartItems = order['get_cart_items']

  components = Component.objects.all()
  context={'components':components, 'cartItems':cartItems}
  return render(request, 'home/home.html',context)

def getComponent(request,cid):
  if request.user.is_authenticated:
    member = request.user.member
    order, created = Order.objects.get_or_create(member=member,complete=False)
    items = order.orderitem_set.all() 
    cartItems = order.get_cart_items
  else:
    items = []
    order = {'get_cart_items':0}
    cartItems = order['get_cart_items']
  component = Component.objects.get(id=cid)
  context={'component':component, 'cartItems':cartItems}
  return render(request, 'home/componentDetail.html',context)

def getDevelopmentBoard(request):
  if request.user.is_authenticated:
    member = request.user.member
    order, created = Order.objects.get_or_create(member=member,complete=False)
    items = order.orderitem_set.all() 
    cartItems = order.get_cart_items
  else:
    items = []
    order = {'get_cart_items':0}
    cartItems = order['get_cart_items']
  component = Component.objects.filter(category='Development Boards')
  context={'components':component, 'cartItems':cartItems}
  return render(request, 'home/home.html',context)

def getSM(request):
  if request.user.is_authenticated:
    member = request.user.member
    order, created = Order.objects.get_or_create(member=member,complete=False)
    items = order.orderitem_set.all() 
    cartItems = order.get_cart_items
  else:
    items = []
    order = {'get_cart_items':0}
    cartItems = order['get_cart_items']
  component = Component.objects.filter(category='Sensors')
  context={'components':component, 'cartItems':cartItems}
  return render(request, 'home/home.html',context)

def getMotor(request):
  if request.user.is_authenticated:
    member = request.user.member
    order, created = Order.objects.get_or_create(member=member,complete=False)
    items = order.orderitem_set.all() 
    cartItems = order.get_cart_items
  else:
    items = []
    order = {'get_cart_items':0}
    cartItems = order['get_cart_items']
  component = Component.objects.filter(category='Motors')
  context={'components':component, 'cartItems':cartItems}
  return render(request, 'home/home.html',context)

def getEC(request):
  if request.user.is_authenticated:
    member = request.user.member
    order, created = Order.objects.get_or_create(member=member,complete=False)
    items = order.orderitem_set.all() 
    cartItems = order.get_cart_items
  else:
    items = []
    order = {'get_cart_items':0}
    cartItems = order['get_cart_items']
  component = Component.objects.filter(category='Electronic Component')
  context={'components':component, 'cartItems':cartItems}
  return render(request, 'home/home.html',context)

def cart(request): 
  if request.user.is_authenticated:
    member = request.user.member
    order, created = Order.objects.get_or_create(member=member,complete=False)
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
    order, created = Order.objects.get_or_create(member=member,complete=False)
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
  print('Component:', componentId," ",type(componentId))
  member = request.user.member
  component = Component.objects.get(id=componentId)
  order, created = Order.objects.get_or_create(member=member,complete=False)
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
  data = json.loads(request.body)
  if request.user.is_authenticated:
    member = request.user.member
    order, created = Order.objects.get_or_create(member=member,complete=False)
    total = data['form']['total']
    #items = data['form']['components']
    orderItems = OrderItem.objects.filter(order=order)
    #print(orderItems)
    if total == str(order.get_cart_items):
      for item in orderItems:
        componentId=item.component.id
        print('Component:', item.component.id," ",type(item.component.id))
        component = Component.objects.get(id=componentId)
        component.stockQunatity = component.stockQunatity-item.quantity
        component.save()
      order.complete = True

    order.save()
  else:
    print('user not logged in...')
  return JsonResponse ('order placed', safe=False)