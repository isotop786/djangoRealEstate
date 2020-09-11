from django.contrib import admin
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display=('id','name','phone','email','is_mvp')
    list_display_links =['name']
    list_editable = ['is_mvp']
    list_filter = ('hire_date',)
    list_per_page = 20
    search_fields = ('name','phone','email')

# Register your models here.
admin.site.register(Realtor,RealtorAdmin)
