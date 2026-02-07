from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, ProfileForm
from core.models import DeliveryTask



def home(request):
    return render(request, 'core/home.html')

def list_view(request):
    return render(request, 'core/list.html')



def register(request):
    if request.method == 'POST':
        uform = RegisterForm(request.POST)
        pform = ProfileForm(request.POST)

        if uform.is_valid() and pform.is_valid():
            user = uform.save(commit=False)
            user.set_password(uform.cleaned_data['password'])
            user.save()

            
            profile = user.profile
            profile.role = pform.cleaned_data['role']
            profile.phone = pform.cleaned_data['phone']
            profile.address = pform.cleaned_data['address']
            profile.save()

            return redirect('login')
    else:
        uform = RegisterForm()
        pform = ProfileForm()

    return render(request, 'core/register.html', {
        'uform': uform,
        'pform': pform
    })



def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        if user:
            login(request, user)
            return redirect('dashboard')

    return render(request, 'core/login.html')


def logout_view(request):
    logout(request)
    return redirect('home')



@login_required
def dashboard(request):
    role = request.user.profile.role

    if role == 'donor':
        return render(request, 'core/donor_dashboard.html')
    elif role == 'ngo':
        return render(request, 'core/ngo_dashboard.html')
    elif role == 'volunteer':
        return render(request, 'core/volunteer_dashboard.html')
    else:
        return redirect('home')

@login_required
def volunteer_dashboard(request):
    tasks = DeliveryTask.objects.filter(status='pending')
    my_tasks = DeliveryTask.objects.filter(volunteer=request.user)
    return render(request, 'core/volunteer_dashboard.html', {
        'tasks': tasks,
        'my_tasks': my_tasks
    })


@login_required
def accept_task(request, task_id):
    task = get_object_or_404(DeliveryTask, id=task_id)
    task.volunteer = request.user
    task.status = 'picked'
    task.save()
    return redirect('volunteer_dashboard')


@login_required
def complete_task(request, task_id):
    task = get_object_or_404(DeliveryTask, id=task_id, volunteer=request.user)
    task.status = 'delivered'
    task.save()
    return redirect('volunteer_dashboard')

