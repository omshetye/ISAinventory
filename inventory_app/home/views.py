from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import json
from .models import *
from django.contrib.auth import authenticate, login, logout
from .backends import OTPBackend
from django.core.mail import send_mail
from django.conf import settings
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
    receipt = f"UserName: {member.name} \n Email: {member.email} \n Total Order Items: {total} \n OrderItems:\n"
    if total == str(order.get_cart_items):
      for item in orderItems:
        componentId=item.component.id
        print('Component:', item.component.id," ",type(item.component.id))
        component = Component.objects.get(id=componentId)
        receipt = receipt + f"{component.name}={item.quantity}\n"
        component.stockQunatity = component.stockQunatity-item.quantity
        component.save()
      order.complete = True

    receipt = receipt + f"Order Id = {order.id}"
    create_text_file(receipt)
    order.save()
    link = f'http://localhost:8000/orders/{order.id}'
    send_mail(
      'Order Approval',
      f'Order Receipt:\n{receipt}\nApprove Order:\n{link}',
      member.email,
      [settings.EMAIL_HOST_USER],
      fail_silently=False
    )
  else:
    print('user not logged in...')
  return JsonResponse ('order placed', safe=False)

def create_text_file(content, output_path='output.txt'):
    with open(output_path, 'w') as file:
        file.write(content)

def getOrder(request,oid):
  order = Order.objects.get(id=oid)
  #orderItem = OrderItem.objects.get(order=order)
  items = order.orderitem_set.all()
  if request.method=='POST':
    orderStatus = request.POST['status']
    order.approval = orderStatus
    order.save()
    send_mail(
      'Order Approved ',
      f'Your order {oid} has been Approved',
      settings.EMAIL_HOST_USER,
      [order.member.email],
      fail_silently=False
    )

  context={'order':order,'items':items}
  return render(request,"home/approval.html",context)




def signin(request):
  err = None
  if request.method=='POST':
      email = request.POST["email"]
      print(email)
      try:
          member = Member.objects.get(email=email)
          otp = member.generate_otp()
          send_mail(
            'OTP verifcation',
            f'{otp} is your OTP verification code.',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False
          )
          request.session['email'] = email
          member.save()
      except Member.DoesNotExist:
          return HttpResponse("User with provided email does not exist!")
      return redirect("verify")
  #     user = OTPBackend.authenticate(request, email=email,otp=otp)
  #     if user is not None:
  #         login(request,user)
  #         return redirect("home")
  #     else:
  #         err = "Invalid Credentials"
  context = {"err":err}
  return render(request,"home/signin.html",context)

def verify(request):
  err = None
  if request.method=='POST':
    otp = request.POST['otp']
    email = request.session['email']
    
    otpBackend = OTPBackend()
    user = otpBackend.authenticate(email=email,otp=otp)
    print(otp,email,user)

    if user is not None:
        otpBackend.login(request,user)
        return redirect("home")
    else:
        err = "OTP did not match"
  context = {"err":err}
  return render(request,"home/verify.html",context)


def signout(request):
  otpBackend = OTPBackend()
  otpBackend.logout(request)
  return redirect("home")