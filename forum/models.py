from django.db import models

# Create your models here.
# forum/models.py
from django.db import models
from django.contrib.auth.models import User

class Thread(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

class Post(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
