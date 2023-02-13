from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter, NumericRangeFilter

admin.site.site_url = 'https://www.texkoop.com'

#waitlist
class WaitListResource(resources.ModelResource):
    class Meta:
        model = Waitlist
        fields = ('id','name','role','email')
        

class WaitlistAdmin(ImportExportModelAdmin):
    
    list_filter = ['role', ('date', DateTimeRangeFilter)]
    list_display = ('name', 'email', 'role', 'date')

    resource_classes = [WaitListResource]
   

#riders
class RidersResource(resources.ModelResource):
    class Meta:
        model = Riders
        fields = '__all__'
        

class RidersAdmin(ImportExportModelAdmin):
    
    list_filter = ['approval_status', ('date', DateTimeRangeFilter)]
    list_display = ['first_name', 'last_name', 'email']
      
    resource_classes = [RidersResource]


#partner
class PartnerResource(resources.ModelResource):
    class Meta:
        model = Partners()
        fields = '__all__'
        

class PartnerAdmin(ImportExportModelAdmin):
    
    list_filter = ['approval_status', ('date', DateTimeRangeFilter)]
    list_display = ['name', 'business_name', 'email']
      
    resource_classes = [PartnerResource]


#Contact us
class ContactUsResource(resources.ModelResource):
    class Meta:
        model = ContactUs()
        fields = '__all__'
        

class ContactUsAdmin(ImportExportModelAdmin):
    
    list_filter = ['read_status', ('date', DateTimeRangeFilter)]
    list_display = ['name', 'email']
      
    resource_classes = [ContactUsResource]

#Article
class FrenchArticleInline(admin.StackedInline):
    model = FrenchArticle
    exclude = ['slug', 'published', 'image', 'date_created','reading_time', 'author']
    extra = 0

class ArticleResource(resources.ModelResource):
    class Meta:
        model = EnglishArticle
        fields = '__all__'
        

class EnglishArticleAdmin(ImportExportModelAdmin):
    exclude = ['slug']
    list_filter = ['author', ('date_created', DateTimeRangeFilter)]
    list_display = ['author', 'title']
    extra = 0

      
    resource_classes = [ArticleResource]    

class ExtendArticleAdmin(EnglishArticleAdmin):
    inlines = EnglishArticleAdmin.inlines + [FrenchArticleInline]

#Author
class AuthorResource(resources.ModelResource):
    class Meta:
        model = ContactUs()
        fields = '__all__'
        
        

class AuthorAdmin(ImportExportModelAdmin):
    
    list_display = ['name']
    # exclude = ['user']  
    resource_classes = [AuthorResource]

#featured article
class FrenchFeaturedMessageAdmin(admin.StackedInline):
    model = FrenchFeaturedMessage
    extra = 0


class FeaturedMessageAdmin(admin.ModelAdmin):
    
    inlines = [FrenchFeaturedMessageAdmin]

    def has_add_permission(self, request):
        MAX_OBJECTS = 1
        if self.model.objects.count() >= MAX_OBJECTS:
            return False
        return super().has_add_permission(request)    


        


admin.site.register(Waitlist, WaitlistAdmin)
admin.site.register(Riders, RidersAdmin)
admin.site.register(Partners, PartnerAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(EnglishArticle, ExtendArticleAdmin)
admin.site.register(FeaturedMessage, FeaturedMessageAdmin)