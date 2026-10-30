from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('fleet/', views.fleet, name='fleet'),
    path('track/', views.track, name='track'),
    path('contact/', views.contact, name='contact'),
]
