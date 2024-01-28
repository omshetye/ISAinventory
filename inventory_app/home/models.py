from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='member')
    name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    isMember = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Component(models.Model):
    name = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=500, null=True)
    stockQunatity = models.IntegerField(default=0, null=True, blank=True)
    category = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Order(models.Model):
    member = models.ForeignKey(Member, on_delete=models.SET_NULL, blank=True, null=True, related_name='member')
    complete = models.BooleanField(default=False, null=True, blank=False)
    date_ordered = models.DateTimeField(auto_now_add=True)
    timeExpiry = models.DateTimeField(auto_now_add=True)
    approval = models.CharField(max_length=20, default='not approved', choices=[('approved', 'Approved'), ('not approved', 'Not Approved')])

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    
class OrderItem (models.Model):
    component = models.ForeignKey (Component, on_delete=models. SET_NULL, null=True)
    order = models.ForeignKey (Order, on_delete=models. SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField (auto_now_add=True)

