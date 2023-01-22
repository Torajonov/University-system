from django.shortcuts import render
from django.views.generic import (
	ListView,
	DetailView,)
from .models import *
# Create your views here.

class HomePageView(ListView):
	template_name = 'index.html'