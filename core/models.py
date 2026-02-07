from django import forms
from django.db import models
from django.contrib.auth.models import User


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
    phone = models.CharField(max_length=15)   # ✅ ADD THIS
    address = models.TextField(blank=True)

    def __str__(self):
        return self.user.username


class DeliveryTask(models.Model):
    STATUS = [
        ('pending', 'Pending'),
        ('picked', 'Picked'),
        ('delivered', 'Delivered'),
    ]

    donation = models.ForeignKey('donations.Donation', on_delete=models.CASCADE)
    request = models.ForeignKey('requests.FoodRequest', on_delete=models.CASCADE)
    volunteer = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=20, choices=STATUS, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)



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
    
class Donation(models.Model):
    donor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='core_donations'   
    )
    food_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    location = models.CharField(max_length=255)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)