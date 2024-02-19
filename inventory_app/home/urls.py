from django.urls import path
from home import views

urlpatterns = [
  path("", views.mainpage, name="home"),
  path("cart/", views.cart, name="cart"),
  path("checkout/", views.checkout, name="checkout"),
  path('update_item/', views.updateItem, name="updateItem"),
  path('process_order/', views.processOrder, name="processOrder"),
  path('development-boards/', views.getDevelopmentBoard, name="getDevelopmentBoard"),
  path('motors/', views.getMotor, name="getMotor"),
  path('sensor/', views.getSM, name="getSM"),
  path('electronic-component/', views.getEC, name="getEC"),
  path('component/<cid>', views.getComponent, name="getComponent"),
  path("signin",views.signin, name="signin"),
  path("verify",views.verify, name="verify"),
  path("signout",views.signout, name="signout"),
  path("orders/<oid>",views.getOrder, name="getOrder"),
  path("pending-orders/<oid>",views.getOrder, name="getOrder"),
  path("profile/", views.getProfile, name="getProfile"),
  path('contact/', views.contact, name='contact'),
  path('success/', views.success, name='success'),
  path('orders/', views.getOrders, name='getOrders'),
  path('pending-orders/', views.getPendingOrders, name='getPendingOrders'),
]
