from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import pyotp
class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='member')
    name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    isMember = models.BooleanField(default=False)
    otp_secret = models.CharField(max_length=16, blank=True, null=True)
    otp_created_at = models.DateTimeField(blank=True, null=True)

    def generate_otp(self):
        self.otp_secret = pyotp.random_base32()
        self.otp_created_at = timezone.now()
        return pyotp.totp.TOTP(self.otp_secret).now()

    def check_otp(self, otp,valid_window=30):
        if self.otp_created_at and self.otp_secret:
            return pyotp.totp.TOTP(self.otp_secret).verify(otp,valid_window=valid_window)
        return False

    def __str__(self):
        return self.name

class Component(models.Model):
    CATEGORY_CHOICES = [
        ('Electronic Component', 'Electronic Component'),
        ('Sensors', 'Sensors'),
        ('Development Boards', 'Development Boards'),
        ('Motors', 'Motors'),
    ]
    name = models.CharField (max_length=200, null=True)
    image = models.ImageField(null=True,blank=True)
    description = models.CharField(max_length=500,null=True)
    stockQunatity = models.IntegerField(default=0,null=True,blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES,null=True,blank=True)
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

