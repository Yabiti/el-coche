from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Car
# Create your views here.

class HomePageView(TemplateView):
    model = Car
    template_name = 'sales/base.html'
