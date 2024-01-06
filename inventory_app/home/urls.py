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
]
