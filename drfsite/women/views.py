from django.shortcuts import render
from rest_framework import generics
from .models import Women
from .serializers import WomenSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict


# Урок 2: Пример простого представления
# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

# Урок 3: Базовый класс APIView 
class WomenAPIView(APIView):
    # Обработка GET-запросов:
    def get(self, request):
        lst = Women.objects.all().values()
        return Response({'posts': list(lst)})
    
    # Обработка POST-запросов:
    def post(self, request):
        post_new = Women.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id'],
        ) 
        return Response({'post': model_to_dict(post_new)})

#     def get(self, request):
#         lst = Women.objects.all().values()
#         return Response({'posts': list(lst)})

#     def post(self, request):
#         post_new = Women.objects.create(
#             title=request.data['title'],
#             content=request.data['content'],
#             cat_id=request.data['cat_id'],
#         )
#         return Response({'post': model_to_dict(post_new)})