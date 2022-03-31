from django.db import models
from django.contrib.auth.models import User


class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_number = models.IntegerField()
    preferred_time = models.IntegerField()
    date = models.DateField()
    booking_for = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Otp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    current_otp = models.IntegerField()

