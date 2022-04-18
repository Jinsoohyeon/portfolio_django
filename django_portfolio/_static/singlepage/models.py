from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Memo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author}::{self.content}'

    def get_absolute_url(self):
        return f'{self.get_absolute_url()}/#memo-{self.pk}/'

class Mail(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    message = models.TextField()
    time_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}::{self.address}::{self.phone}::{self.time_at}'