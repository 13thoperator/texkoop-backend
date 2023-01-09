from django.contrib import admin
from .models import *

admin.site.site_url = 'https://www.texkoop-incoming.vercel.app'

class WaitlistAdmin(admin.ModelAdmin):
    list_filter = ['role']
    list_display = ('name', 'email', 'role', 'date')

admin.site.register(Waitlist, WaitlistAdmin)