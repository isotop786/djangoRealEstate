from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing
from realtors.models import Realtor
from listings.choices import bedroom_choices,price_choices,state_choices
# Create your views here.

def index(request):
    listing = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listing':listing,
        'states':state_choices,
        'prices':price_choices,
        'bedrooms':bedroom_choices
    }

    return render(request,'pages/index.html',context)

def about(request):
    realtors = Realtor.objects.order_by('-hire_date')

    mvp = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtor':realtors,
        'mvp':mvp
    }
    return render(request,'pages/about.html',context)