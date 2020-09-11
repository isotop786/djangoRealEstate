from django.shortcuts import render,get_object_or_404
from .models import Listing
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from listings.choices import bedroom_choices,state_choices,price_choices
# Create your views here.

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    # per page 3 lising
    paginator = Paginator(listings,6)
    # getting pages
    page = request.GET.get('page')

    paged_listings = paginator.get_page(page)


    context = {
        'listings':paged_listings,
        'state_choices':state_choices,
        'prices':price_choices,
        'bedrooms':bedroom_choices
    }

    return render(request,'listings/listings.html',context)

def listing(request,listing_id):
    # listing = Listing.objects.get(id=listing_id)
    listing =get_object_or_404(Listing,pk=listing_id)

    context ={
        'listing':listing
    }
    return render(request,'listings/listing.html',context)    
def search(request):
    query_set =Listing.objects.order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        words = request.GET['keywords']
        if words:
            query_set = query_set.filter(description__icontains=words)
    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            query_set = query_set.filter(city__iexact=city)    
    # State 
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            query_set = query_set.filter(state__iexact=state)                    
    # Bedrooms 
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            query_set = query_set.filter(bedrooms__lte=bedrooms)
    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            query_set = query_set.filter(price__lte=price)        
    context = {
        'bedrooms':bedroom_choices,
        'states':state_choices,
        'prices':price_choices,
        'listings':query_set,
        'value':request.GET
    }
    return render(request,'listings/search.html',context)    