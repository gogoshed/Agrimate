from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional fields for the user profile

# views.py
@login_required
def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    # Your profile view code here


# Create your models here.
