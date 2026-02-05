from django import forms
from .models import Donation


class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['food_name', 'quantity', 'pickup_location']
        widgets = {
            'food_name': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'pickup_location': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
        }
