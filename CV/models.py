from cProfile import label
from email.message import Message
from logging import PlaceHolder
from django.db import models

# Create your models here.

class Mail(models.Model):
    name = models.CharField(max_length=100,help_text="Name")
    email = models.EmailField(help_text="Email",max_length=100)
    phone = models.CharField(help_text="Phone",max_length=100)
    subject = models.CharField(help_text="Subject",max_length=100)
    message = models.TextField(help_text="Message")
