import email
import re

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


# class MailList(models.Model):
    
#     email = models.EmailField()
#     date_subscribed = models.DateTimeField(auto_now_add=True)
    

#     def __str__(self):
#         return self.email


# class Newsletter(models.Model):
#     title = models.CharField(max_length=300, default='enter title')
#     body =RichTextUploadingField(default='Empty Content')
#     date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

#     def __str__(self):
#         return self.title


# class Category(models.Model):
#     english_name = models.CharField(max_length=100)
#     french_name = models.CharField(max_length=100)
#     eng_slug = models.SlugField()
#     fr_slug = models.SlugField()

#     class Meta:
#         verbose_name_plural = 'Categories'


#     def __str__(self):
#         return self.english_name

#     def save(self, *args, **kwargs):
#         self.eng_slug = re.sub(r"\s+", '-', self.english_name.lower())
#         self.fr_slug = re.sub(r"\s+", '-', self.french_name.lower())
#         super().save(*args, **kwargs)    


# class EnglishArticle(models.Model):
#     slug = models.SlugField()
#     title = models.CharField(max_length=300)
#     category = models.ForeignKey(Category, related_name='english_category', on_delete=models.CASCADE)
#     body = RichTextUploadingField(default='Empty Content')
#     date_created = models.DateTimeField()
#     published = models.BooleanField(default=False)
#     image = models.ImageField(blank = True, null = True)

#     class Meta:
#         verbose_name_plural = 'Articles'

#     def __str__(self):
#         return self.title

#     def save(self, *args, **kwargs):
#         self.slug = re.sub(r"\s+", '-', self.title.lower())
#         super().save(*args, **kwargs)
    


# class FrenchArticle(models.Model):
#     slug = models.SlugField()
#     title = models.CharField(max_length=300)
#     category = models.ForeignKey(Category, related_name='french_category', on_delete=models.CASCADE)
#     body = RichTextUploadingField(default='Empty Content')
#     date_created = models.DateTimeField()
#     published = models.BooleanField(default=False)
#     image = models.ImageField(blank = True, null = True)
#     english_article = models.OneToOneField(
#         EnglishArticle,
#         related_name="english_article",
#         blank=True,
#         null=True,
#         on_delete=models.CASCADE)

#     class Meta:
#         verbose_name_plural = 'French Articles'    


#     def __str__(self):
#         return self.title

#     def save(self, *args, **kwargs):
#         self.slug = re.sub(r"\s+", '-', self.title.lower())
#         self.published = self.english_article.published
#         self.category = self.english_article.category
#         self.image = self.english_article.image
#         self.date_created = self.english_article.date_created
#         super().save(*args, **kwargs)



# class Riders(models.Model):
#     APPROVAL_CHOICES = (
#         ('pending', 'pending'),
#         ('approved', 'approved'),
#         ('disapproved', 'disapproved'),
#     )
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)
#     email = models.EmailField()
#     telephone_number = models.CharField(max_length=20)
#     city = models.CharField(max_length=200)
#     approval_status = models.CharField(
#         'Approval Status',
#         max_length=11,
#         choices=APPROVAL_CHOICES,
#         default='pending')
#     date = models.DateTimeField(auto_now_add=True)      

#     class Meta:
#         verbose_name_plural = 'Riders'

    


# class Partners(models.Model):
#     APPROVAL_CHOICES = (
#         ('pending', 'pending'),
#         ('approved', 'approved'),
#         ('disapproved', 'disapproved'),
#     )
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)
#     company_name = models.CharField(max_length=400)
#     email = models.EmailField()
#     telephone_number = models.CharField(max_length=20)
#     approval_status = models.CharField(
#         'Approval Status',
#         max_length=11,
#         choices=APPROVAL_CHOICES,
#         default='pending')
#     date = models.DateTimeField(auto_now_add=True)   

#     class Meta:
#         verbose_name_plural = 'Partners'   
    
# class Clients(models.Model):
#     APPROVAL_CHOICES = (
#         ('pending', 'pending'),
#         ('approved', 'approved'),
#         ('disapproved', 'disapproved'),
#     )
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)
#     company_name = models.CharField(max_length=400)
#     email = models.EmailField()
#     telephone_number = models.CharField(max_length=20)
#     approval_status = models.CharField(
#         'Approval Status',
#         max_length=11,
#         choices=APPROVAL_CHOICES,
#         default='pending')
#     date = models.DateTimeField(auto_now_add=True)   

#     class Meta:
#         verbose_name_plural = 'Clients'   


   
# class ContactUs(models.Model):
#     READ_CHOICES = (
#         ('pending', 'pending'),
#         ('read', 'read'),
        
#     )
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)
#     email = models.EmailField()
#     telephone_number = models.CharField(max_length=20)
#     message = models.TextField()
#     read_status = models.CharField(
#         'Read Status',
#         max_length=11,
#         choices=READ_CHOICES,
#         default='pending')
#     date = models.DateTimeField(auto_now_add=True)   

#     class Meta:
#         verbose_name_plural = 'Contact Us' 



class Waitlist(models.Model):
    
    name = models.CharField(max_length=200)
    email = models.EmailField()
    role = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)   
    

    class Meta:
        verbose_name_plural = 'Waitlist'

    def __str__(self):
            return self.name    