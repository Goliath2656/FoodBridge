from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import DonationForm
from .models import Donation



@login_required
def add_donation(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.donor = request.user
            donation.save()
            return redirect('list_donations')
    else:
        form = DonationForm()

    return render(request, 'donations/add.html', {'form': form})


@login_required
def list_donations(request):
    if request.user.profile.role == 'donor':
        donations = Donation.objects.filter(donor=request.user)
    else:
        donations = Donation.objects.all()

    return render(request, 'donations/list.html', {'donations': donations})




