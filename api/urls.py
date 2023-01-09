from django.urls import path
from .views import *


app_name = "api"
urlpatterns = [
    # path('contact-us/', contact_us_create, name='contact-us'),
    # path('rider/', rider_create, name='rider'),
    # path('client/', client_create, name='client'),
    # path('partner/', partner_create, name='partner'),
    # path('recent-post-categories/', latest_articles_and_categories, name='recent-post-categories'),
    # path('articles/', articles, name='articles')
     path('api/waitlist/', waitlist_create, name='waitlist'),
     path('', homepage, name='homepage')
]