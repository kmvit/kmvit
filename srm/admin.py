from django.contrib import admin
from .models import *
# Register your models here.


class DealAdmin(admin.ModelAdmin):
    list_display=['title','contact','born', 'prepayment', 'budget']
    date_hierarchy = 'born'
    list_filter = ['stage','contact' ]
    
    
    
admin.site.register(Contact)    
admin.site.register(City)   
admin.site.register(Stage)
admin.site.register(Deal, DealAdmin)
