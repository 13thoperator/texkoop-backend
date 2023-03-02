
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from .paginations import *
# Create your views here.


def homepage(request):
    return redirect('/admin')
    

@api_view(['POST'])
def contact_us_create(request):
    try:
    
        serializer = ContactUsSerializer(data=request.data)
        if serializer.is_valid():
            
            serializer.save()
            return Response({
                "success": True 
            }, status=status.HTTP_201_CREATED)

        else:
            return Response({
                "success": False
            }, status=status.HTTP_400_BAD_REQUEST)  
    except Exception as e:
       
        return Response({
            "success": False
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)          

    

@api_view(['POST'])
def rider_create(request):
    try:
    
        serializer = RiderSerializer(data=request.data)
        if serializer.is_valid():
            
            serializer.save()
            return Response({
                "success": True 
            }, status=status.HTTP_201_CREATED)

        else:
            return Response({
                "success": False
            }, status=status.HTTP_400_BAD_REQUEST) 
    except Exception as e:
       
        return Response({
            "success": False
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)           



@api_view(['POST'])
def partner_create(request):
    try:
    
        serializer = PartnerSerializer(data=request.data)
        if serializer.is_valid():
            
            serializer.save()
            return Response({
                "success": True 
            }, status=status.HTTP_201_CREATED)

        else:
            return Response({
                "success": False
            }, status=status.HTTP_400_BAD_REQUEST) 
    except Exception as e:
       
        return Response({
            "success": False
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)           



@api_view(['GET'])
def top_articles(request):
    try: 
        articles = EnglishArticle.objects.filter(published = True).order_by('views')[:3]
        articles_serializer = EnglishArticleSerializer(articles, many = True)
        
        return Response({
            "success": True,
            "articles": articles_serializer.data,
            
        }, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response({
            "success": False
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def articles(request):
    try: 
        articles =EnglishArticle.objects.filter(published = True).order_by('-id')
        
        paginator =  CustomPagination()
        data = paginator.paginate_queryset(articles, request)
        # data = CustomPagination().paginate_queryset(articles, request)
        articles_serializer = EnglishArticleSerializer(data, many = True)
        return paginator.get_paginated_response(articles_serializer.data)
        # return Response({
        #     "success": True,
        #     "articles": articles_serializer.data,
            
        # }, status=status.HTTP_200_OK)
    
    except Exception as e:
       
        return Response({
            "success": False
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def article(request, slug):
    try: 
        article =EnglishArticle.objects.get(published = True, slug=slug)
        article.views +=1
        article.save()
        article_serializer = EnglishArticleSerializer(article, many = False)

        
        
        return Response({
            "success": True,
            "article": article_serializer.data,
            
            
        }, status=status.HTTP_200_OK)
    
    except Exception as e:
        
        return Response({
            "success": False
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)        



@api_view(['GET'])
def featuredMessage(request):
    try: 
        featured_article = FeaturedMessage.objects.all().first()
        featured_message_serializer = FeaturedMessageSerializer(featured_article, many = False) 
        return Response({
            "success": True,
            "featuredMessage": featured_message_serializer.data,
            
        }, status=status.HTTP_200_OK)
    
    except Exception as e:
       
        return Response({
            "success": False
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def waitlist_create(request):
    try:
        serializer = WaitlistSerializer(data=request.data)
        if serializer.is_valid():
            
            serializer.save()
            return Response({
                "success": True 
            }, status=status.HTTP_201_CREATED)

        else:
            
            return Response({
                "success": False
            }, status=status.HTTP_400_BAD_REQUEST) 
    except Exception as e:
       
        return Response({
            "success": False
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)       



@api_view(['POST'])
def app_waitlist_create(request):
    try:
        serializer = AppWaitlistSerializer(data=request.data)
        if serializer.is_valid():
            
            serializer.save()
            return Response({
                "success": True 
            }, status=status.HTTP_201_CREATED)

        else:
            
            return Response({
                "success": False
            }, status=status.HTTP_400_BAD_REQUEST) 
    except Exception as e:
       
        return Response({
            "success": False
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)         


