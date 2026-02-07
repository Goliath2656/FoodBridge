from django.db import models
from django.contrib.auth.models import User

class Donation(models.Model):
    donor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='donations'
    )
    food_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    pickup_location = models.CharField(max_length=255)  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.food_name

