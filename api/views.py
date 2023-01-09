
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


def homepage(request):
    return redirect('/admin')
    

# @api_view(['POST'])
# def contact_us_create(request):
    
#     serializer = ContactUsSerializer(data=request.data)
#     if serializer.is_valid():
        
#         serializer.save()
#         return Response({
#             "success": True 
#         }, status=status.HTTP_201_CREATED)

#     else:
#         return Response({
#             "success": False
#         }, status=status.HTTP_400_BAD_REQUEST)    

    

# @api_view(['POST'])
# def rider_create(request):
    
#     serializer = RiderSerializer(data=request.data)
#     if serializer.is_valid():
        
#         serializer.save()
#         return Response({
#             "success": True 
#         }, status=status.HTTP_201_CREATED)

#     else:
#         return Response({
#             "success": False
#         }, status=status.HTTP_400_BAD_REQUEST)    



# @api_view(['POST'])
# def partner_create(request):
    
#     serializer = PartnerSerializer(data=request.data)
#     if serializer.is_valid():
        
#         serializer.save()
#         return Response({
#             "success": True 
#         }, status=status.HTTP_201_CREATED)

#     else:
#         return Response({
#             "success": False
#         }, status=status.HTTP_400_BAD_REQUEST)    


# @api_view(['POST'])
# def client_create(request):
    
#     serializer = ClientSerializer(data=request.data)
#     if serializer.is_valid():
        
#         serializer.save()
#         return Response({
#             "success": True 
#         }, status=status.HTTP_201_CREATED)

#     else:
#         return Response({
#             "success": False
#         }, status=status.HTTP_400_BAD_REQUEST)    


# @api_view(['GET'])
# def latest_articles_and_categories(request):
#     try: 
#         articles =EnglishArticle.objects.filter(published = True).order_by('id')[:3]
#         articles_serializer = EnglishArticleSerializer(articles, many = True)
#         categories = Category.objects.all()
#         categories_serializer = CategorySerializer(categories, many=True)
#         return Response({
#             "success": True,
#             "latest_articles": articles_serializer.data,
#             "categories": categories_serializer.data
#         }, status=status.HTTP_200_OK)
    
#     except Exception as e:
#         return Response({
#             "success": False
#         }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# @api_view(['GET'])
# def articles(request):
#     # try:
#     articles = EnglishArticle.objects.filter(published = True).order_by("id")
#     paginator = PageNumberPagination()
#     result = paginator.paginate_queryset(articles, request)
#     serializer = EnglishArticleSerializer(result, many=True)
#     return paginator.get_paginated_response(serializer.data)
    # except Exception as e:
    #     return Response({
    #         "success": False,
            
    #     }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def waitlist_create(request):
    
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
