from django.db import models

# Create your models here.
from django.contrib.auth.models import User

# etelaati ke hsksi ke drkhast ye code jadid dade ke brash code drst beshe ro zkhire mikonim
class Passwordresetcodes(models.Model):
    code = models.CharField(max_length=32)
    email = models.CharField(max_length=120)
    time = models.DateTimeField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)  # TODO: do not save password


class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=48)

    def __str__(self):
        return "{}_token".format(self.user)


class Expense(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    def __str__(self):
        return "{}-{}-{}".format(self.date,self.user, self.amount)

class Income(models.Model):
    def __str__(self):
        return "{}-{}".format(self.date, self.amount)
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    def __str__(self):
        return "{}-{}-{}".format(self.date,self.user, self.amount)
