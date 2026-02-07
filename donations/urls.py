from django.urls import path
from . import views


urlpatterns = [
    
    path('add/', views.add_donation, name='add_donation'),
    path('list/', views.donation_list, name='donation_list'),

]