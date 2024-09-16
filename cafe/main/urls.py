from django.urls import path, include
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact_view, name='contact'),
    path('coffees/', CoffeesListView.as_view(), name='coffees'),
    path('success/', TemplateView.as_view(template_name='success.html'), name='success'),
]