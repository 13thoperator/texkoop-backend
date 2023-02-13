from django.urls import path
from .views import *


app_name = "api"
urlpatterns = [
    path('contact-us/', contact_us_create, name='contact-us'),
    path('rider/', rider_create, name='rider'),
    path('partner/', partner_create, name='partner'),
    # path('recent-post-categories/', latest_articles_and_categories, name='recent-post-categories'),
    path('api/featured-message/', featuredMessage, name='featured-message'),
    path('api/top-articles/', top_articles, name='top-articles'),
    path('api/articles/', articles, name='articles'),
    path('api/article/<slug:slug>/', article, name='article'),
     path('api/waitlist/', waitlist_create, name='waitlist'),
     path('', homepage, name='homepage')
]