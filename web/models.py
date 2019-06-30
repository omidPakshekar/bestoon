from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Expense(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
class Income(models.Model):
    def __str__(self):
        return "{}-{}".format(self.date, self.amount)
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    def __str__(self):
        return "{}-{}".format(self.date, self.amount)
