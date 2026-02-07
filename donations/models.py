from django.db import models
from django.contrib.auth.models import User

class Donation(models.Model):
    donor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='donation_app_donations'  
    )
    food_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()

