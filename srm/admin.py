from django.contrib import admin
from .models import *
# Register your models here.


class DealAdmin(admin.ModelAdmin):
    list_display = ['title', 'name', 'company','city', 'site', 'stage', 'prepayment', 'prepayment_date', 'remainder', 'budget']
    empty_value_display = '-empty-'
    list_editable = ['stage']
    date_hierarchy = 'born'
    list_filter = ['stage','company']
    
    
    
    
admin.site.register(City)   
admin.site.register(Stage)
admin.site.register(Deal, DealAdmin)