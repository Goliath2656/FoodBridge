from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RequestForm
from .models import FoodRequest


@login_required
def add_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            req = form.save(commit=False)
            req.ngo = request.user
            req.save()
            return redirect('list_requests')
    else:
        form = RequestForm()

    return render(request, 'requests/add.html', {'form': form})



@login_required
def list_requests(request):
    if request.user.profile.role == 'ngo':
        requests = FoodRequest.objects.filter(ngo=request.user)
    else:
        requests = FoodRequest.objects.all()

    return render(request, 'requests/list.html', {'requests': requests})

