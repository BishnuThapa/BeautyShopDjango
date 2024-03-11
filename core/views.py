from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    sliders = Slider.objects.all()
    brands = Brand.objects.all()
    context = {
        'sliders': sliders,
        'brands': brands
    }
    return render(request, 'core/index.html', context)


def shop(request):
    return render(request, 'core/shop.html')


def categorylist(request):
    return render(request, 'core/category-list.html')
