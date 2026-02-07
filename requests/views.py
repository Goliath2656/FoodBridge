from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RequestForm
from .models import FoodRequest
from core.models import Donation
from core.models import DeliveryTask


@login_required
def add_request(request):
    form = RequestForm(request.POST or None)
    if form.is_valid():
        req = form.save(commit=False)
        req.ngo = request.user
        req.save()

        donation = Donation.objects.filter(
            food_name=req.food_required,
            is_available=True
        ).first()

        if donation:
            DeliveryTask.objects.create(
                donation=donation,
                request=req
            )
            donation.is_available = False
            donation.save()

        return redirect('add_request')

    return render(request, 'requests/add.html', {'form': form})



@login_required
def list_requests(request):
    if request.user.profile.role == 'ngo':
        requests = FoodRequest.objects.filter(ngo=request.user)
    else:
        requests = FoodRequest.objects.all()

    return render(request, 'requests/list.html', {'requests': requests})

