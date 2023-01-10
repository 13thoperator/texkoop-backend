from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter, NumericRangeFilter

admin.site.site_url = 'https://www.texkoop-incoming.vercel.app'

class WaitListResource(resources.ModelResource):
    class Meta:
        model = Waitlist
        fields = ('id','name','role','email')
        

class WaitlistAdmin(ImportExportModelAdmin):
    
    list_filter = ['role', ('date', DateTimeRangeFilter)]
    list_display = ('name', 'email', 'role', 'date')
   
    
    resource_classes = [WaitListResource]

admin.site.register(Waitlist, WaitlistAdmin)