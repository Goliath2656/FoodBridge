from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import DonationForm
from .models import Donation



@login_required
def add_donation(request):
    form = DonationForm(request.POST or None)
    if form.is_valid():
        donation = form.save(commit=False)
        donation.donor = request.user
        donation.save()
        return redirect('donation_list')
    return render(request, 'donations/add.html', {'form': form})


@login_required
def donation_list(request):
    donations = Donation.objects.all()
    return render(request, 'donations/list.html', {'donations': donations})




