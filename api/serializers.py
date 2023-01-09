from dataclasses import fields
from os import read
from statistics import mode
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User



# class ContactUsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ContactUs
#         fields = '__all__'


# class RiderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Riders
#         fields = ['first_name', 'last_name', 'email', 'city', 'telephone_number']


# class PartnerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Partners
#         fields = ['first_name', 'last_name', 'email', 'company_name', 'telephone_number']


# class ClientSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Clients
#         fields = ['first_name', 'last_name', 'email', 'company_name', 'telephone_number']     

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ['english_name', 'french_name', 'eng_slug', 'fr_slug']


# class FrenchArticleSerializer(serializers.ModelSerializer):
#     category = CategorySerializer(read_only = True)
#     class Meta:
#         model = FrenchArticle
#         fields = ['title', 'body', 'category', 'slug', 'date_created', 'published', 'image']


# class EnglishArticleSerializer(serializers.ModelSerializer):
#     english_article = FrenchArticleSerializer(read_only=True)
#     category = CategorySerializer(read_only = True)
#     class Meta:
#         model = EnglishArticle
#         fields = ['title', 'body', 'category', 'slug', 'date_created', 'published', 'image', 'english_article']


class WaitlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waitlist
        fields = ['name', 'email', 'role', ]