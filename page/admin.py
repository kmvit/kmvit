from django.contrib import admin
from .models import *
# Register your models here.

class SectionInline(admin.StackedInline):
    model = Section

class PageAdmin(admin.ModelAdmin):
    inlines = [ SectionInline, ]

 
admin.site.register(Page, PageAdmin)
admin.site.register(Whoweare)
admin.site.register(Whatwedo)
admin.site.register(Fact)
admin.site.register(Lastwork)
admin.site.register(Expectbest)
admin.site.register(Team)
admin.site.register(Review)
admin.site.register(Banner)
admin.site.register(FeedBack)