from django.contrib.auth.backends import ModelBackend
from .models import Member  
from django.contrib.auth import login as django_login, logout as django_logout
class OTPBackend(ModelBackend):
    def authenticate(self, email=None, otp=None, **kwargs):
        try:
            member = Member.objects.get(email=email)
            print(member,member.otp_secret,member.otp_created_at)
            if member.check_otp(otp):
                return member.user
        except Member.DoesNotExist:
            return None
        
    def login(self, request, user):
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        django_login(request, user)

    def logout(self, request):
        django_logout(request)