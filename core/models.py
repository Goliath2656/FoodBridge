from django.db import models
from django.contrib.auth.models import User
from django import forms


class Profile(models.Model):
    ROLE_CHOICES = [
        ('donor', 'Food Donor'),
        ('ngo', 'NGO'),
        ('volunteer', 'Volunteer'),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.user.username
    


class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Create a password'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email address'
            }),
        }

class DeliveryTask(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('picked', 'Picked Up'),
        ('delivered', 'Delivered'),
    ]

    
    donation = models.ForeignKey(
        'donations.Donation',
        on_delete=models.CASCADE,
        related_name='delivery_tasks'
    )

    
    request = models.ForeignKey(
        'requests.FoodRequest',
        on_delete=models.CASCADE,
        related_name='delivery_tasks'
    )

    
    volunteer = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_tasks'
    )

   
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    picked_at = models.DateTimeField(null=True, blank=True)
    delivered_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"DeliveryTask #{self.id} ({self.status})"
