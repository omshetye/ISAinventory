# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('home.urls'))
# ]
from django.urls import path
from home import views

urlpatterns = [
  path("cart/", views.cart, name="cart"),
  path("checkout/", views.checkout, name="checkout"),
  path("", views.mainpage, name="home"),
]
