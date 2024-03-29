from django.db import models
from django.contrib.auth.models import User
from users.models import Profile

# Create your models here.

class ThreadModel(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='+')
    receiver =models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='+')

class MessageModel(models.Model):
    thread = models.ForeignKey('ThreadModel', related_name='+', on_delete=models.CASCADE, blank=True, null=True)
    sender_user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='+')
    receiver_user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='+')
    body = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='message_images', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
