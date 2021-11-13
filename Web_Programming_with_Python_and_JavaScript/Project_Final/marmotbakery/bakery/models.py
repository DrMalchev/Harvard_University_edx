
import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class User(AbstractUser):
    pass

class Orders(models.Model):
    breadType = (
        ('White Bread', 'White Bread'),
        ('Country Bread', 'Country Bread'),
        ('Oat Porridge Bread', 'Oat Porridge Bread'),
        ('Semolina Bread', 'Semolina Bread'),
        ('100% Rye Bread', '100% Rye Bread'),
        ('Focaccia', 'Focaccia'),
        ('Toast Bread', 'Toast Bread'),
        ('Sweet Brioche', 'Sweet Brioche')
    )

    firstName = models.CharField(max_length=64)
    lastName = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    postCode = models.IntegerField()
    addressL1 = models.CharField(max_length=64)
    addressL2 = models.CharField(max_length=64)
    comment = models.CharField(max_length=256)
    breadType = models.CharField(max_length=64, choices=breadType)
    quantity = models.IntegerField(default=0, null=False)
    tel = models.IntegerField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    price = models.CharField(default=0, max_length=64)
    orderTime = models.DateTimeField(default=datetime.datetime.now)
    cumulative = models.IntegerField(default=0)
    brake = models.BooleanField(default=False)
    deliveryTime = models.DateTimeField(default=datetime.datetime.now)

