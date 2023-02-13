from dataclasses import fields
from os import read
from statistics import mode
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User



class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'


class RiderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Riders
        fields = ['first_name', 'last_name', 'email', 'city', 'phone_number', 'message']


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partners
        fields = ['name', 'email', 'business_name', 'phone_number', 'country', 'city', 'industry', 'delivery_volume', 'message']


# class ClientSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Clients
#         fields = ['first_name', 'last_name', 'email', 'company_name', 'telephone_number']     

class FrenchFeaturedMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrenchFeaturedMessage
        fields = '__all__'

class FeaturedMessageSerializer(serializers.ModelSerializer):
    french_message = FrenchFeaturedMessageSerializer(read_only=True)
    
    class Meta:
        model = FeaturedMessage
        fields = ['title', 'body', 'french_message', 'image']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'image']


class FrenchArticleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FrenchArticle
        fields = ['title', 'body']


class EnglishArticleSerializer(serializers.ModelSerializer):
    author =  AuthorSerializer(read_only=True)
    french_article = FrenchArticleSerializer(read_only=True)
    
    class Meta:
        model = EnglishArticle
        fields = ['title', 'body', 'reading_time', 'slug', 'date_created', 'image', 'french_article', 'author']


class WaitlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waitlist
        fields = ['name', 'email', 'role', ]