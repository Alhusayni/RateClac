from django.db import models
from django.utils import timezone


# Create your models here.

class Calculator(models.Model):
    isSup = (
        ('Yes', 'نعم'),
        ('No', 'لا')
    )
    Price = models.PositiveBigIntegerField()
    Salary = models.PositiveBigIntegerField()
    Years = models.PositiveBigIntegerField()
    DownPay = models.PositiveBigIntegerField()
    IntrestRate = models.FloatField()
    isSupported = models.CharField(max_length=100, choices=isSup, default='')
    timestamp = models.DateTimeField(default=timezone.now())