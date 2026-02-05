from django.db import models
from django.contrib.auth.models import User


class FoodRequest(models.Model):
    URGENCY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    ngo = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='food_requests'
    )
    food_required = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    urgency = models.CharField(max_length=10, choices=URGENCY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    is_fulfilled = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.food_required} ({self.quantity})"

