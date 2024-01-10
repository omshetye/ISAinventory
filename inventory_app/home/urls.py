# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('home.urls'))
# ]
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
]
