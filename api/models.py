import email
import re
from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

# Create your models here.


class FeaturedMessage(models.Model):
    title = models.CharField(max_length=1000)
    body = RichTextUploadingField()
    image = models.ImageField()

    def __str__(self):
        return self.title

class FrenchFeaturedMessage(models.Model):
    french_message = models.OneToOneField(
        FeaturedMessage,
        related_name="french_message",
        blank=True,
        null=True,
        on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    body = RichTextUploadingField()
    


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    image = models.ImageField()
    bio = models.TextField()

    def __str__(self):
        return self.name

    
class EnglishArticle(models.Model):
    author = models.ForeignKey(Author, related_name='author',on_delete=models.SET_NULL, null=True) 
    slug = models.SlugField()
    title = models.CharField(max_length=300)
    body = RichTextUploadingField(default='Empty Content')
    date_created = models.DateField()
    published = models.BooleanField(default=False)
    image = models.ImageField(blank = True, null = True)
    reading_time = models.IntegerField()
    views = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        title = self.title.lower()
        x = ['@', '#', '?', "/", ".", ",", "&", "!","|","-","_"]
        z ="".join(filter(lambda char: char not in x, title)) 
        self.slug = re.sub(r"\s+", '-', z)
        super().save(*args, **kwargs)
    


class FrenchArticle(models.Model):
    title = models.CharField(max_length=300)
    body = RichTextUploadingField(default='Empty Content')
    french_article = models.OneToOneField(
        EnglishArticle,
        related_name="french_article",
        blank=True,
        null=True,
        on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'French Articles'    


    def __str__(self):
        return self.title

    



class Riders(models.Model):
    APPROVAL_CHOICES = (
        ('pending', 'pending'),
        ('approved', 'approved'),
        ('disapproved', 'disapproved'),
    )
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    city = models.CharField(max_length=200)
    message = models.TextField()
    approval_status = models.CharField(
        'Approval Status',
        max_length=11,
        choices=APPROVAL_CHOICES,
        default='pending')
    date = models.DateTimeField(auto_now_add=True)      

    class Meta:
        verbose_name_plural = 'Riders'

    


class Partners(models.Model):
    APPROVAL_CHOICES = (
        ('pending', 'pending'),
        ('approved', 'approved'),
        ('disapproved', 'disapproved'),
    )
    name = models.CharField(max_length=200)
    business_name = models.CharField(max_length=400)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    industry = models.CharField(max_length=200)
    delivery_volume = models.CharField(max_length=200)
    message = models.TextField()
    approval_status = models.CharField(
        'Approval Status',
        max_length=11,
        choices=APPROVAL_CHOICES,
        default='pending')
    date = models.DateTimeField(auto_now_add=True)   

    class Meta:
        verbose_name_plural = 'Partners'   
    


   
class ContactUs(models.Model):
    READ_CHOICES = (
        ('pending', 'pending'),
        ('read', 'read'),
        
    )
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    city = models.CharField(max_length=200)
    message = models.TextField()
    read_status = models.CharField(
        'Read Status',
        max_length=11,
        choices=READ_CHOICES,
        default='pending')
    date = models.DateTimeField(auto_now_add=True)   

    class Meta:
        verbose_name_plural = 'Contact Us' 



class Waitlist(models.Model):
    
    name = models.CharField(max_length=200)
    email = models.EmailField()
    role = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)   
    

    class Meta:
        verbose_name_plural = 'Waitlist'

    def __str__(self):
            return self.name    


class AppWaitlist(models.Model):
    
    name = models.CharField(max_length=200)
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)   
    role = models.CharField(max_length=200, default="Individual")
    

    class Meta:
        verbose_name_plural = 'App Waitlist'

    def __str__(self):
            return self.name    