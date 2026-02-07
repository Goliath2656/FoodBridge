from django import forms
from .models import FoodRequest

class RequestForm(forms.ModelForm):
    class Meta:
        model = FoodRequest
        fields = ['food_required', 'quantity', 'urgency']
        widgets = {
            'food_required': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Rice, Meals, Bread'
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'urgency': forms.Select(attrs={
                'class': 'form-control'
            }),
        }

