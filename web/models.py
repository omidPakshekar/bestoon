from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Expense(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
 
