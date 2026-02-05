from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('list/', views.list_view, name='list'),
    
    path('volunteer/tasks/', views.volunteer_tasks, name='volunteer_tasks'),
    path('volunteer/history/', views.volunteer_history, name='volunteer_history'),

    path('task/accept/<int:task_id>/', views.accept_task, name='accept_task'),
    path('task/complete/<int:task_id>/', views.complete_task, name='complete_task'),
    
    
]
