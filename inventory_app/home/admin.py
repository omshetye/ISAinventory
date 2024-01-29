# from django.contrib import admin
# from .models import *
# # Register your models here.
# admin.site.register(Member)
# admin.site.register(Component)
# admin.site.register(Order)
# admin.site.register(OrderItem)

from django.contrib import admin
from django.conf import settings
from django.core.mail import send_mail
from .models import Member, Component, Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'member', 'complete', 'date_ordered','approval']
    inlines = [OrderItemInline]

    def save_model(self, request, obj, form, change):
        # Record the approval status
        if 'approval' in form.changed_data:
            # 'complete' field has been changed
            complete = form.cleaned_data['approval']
            # Perform any additional logic related to the change in 'complete'

            # Example: Send an email to the user
            if complete:
                member_email = obj.member.email if obj.member else ''
                send_mail(
                    'Order Status Update',
                    f'Your order {obj.id} has been marked as {complete}.',
                    settings.EMAIL_HOST_USER,
                    [member_email],
                    fail_silently=False,
                )

        super().save_model(request, obj, form, change)

admin.site.register(Member)
admin.site.register(Component)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
