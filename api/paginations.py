from rest_framework.response import Response
from rest_framework import pagination
from rest_framework.pagination import PageNumberPagination

class CustomPagination(pagination.PageNumberPagination):

    page_size = 2
    page_query_param = 'p'
    page_size_query_param = 'page_size'
    limit_query_param='l'
    max_page_size = 8


    def get_paginated_response(self, data):
        
        response = Response(data)

        return Response(
            {
                "result": data,
                "count": self.page.paginator.count,
                "next": self.get_next_link(),
                "previous": self.get_previous_link()
            }
        )
        # return response

