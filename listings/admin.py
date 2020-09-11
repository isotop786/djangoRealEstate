from django.contrib import admin
from .models import Listing


# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display =('id','title','is_published','price','realtor')
    list_display_links= ('id','title')
    list_editable= ['is_published']
    list_filter = ('realtor','list_date','price')
    search_fields = ('title','description','city','zipcode','price')
    list_per_page = 20

admin.site.register(Listing,ListingAdmin)

