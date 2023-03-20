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
# class WomenAPIView(APIView):
#     # Обработка GET-запросов:
#     def get(self, request):
#         lst = Women.objects.all().values()
#         return Response({'posts': list(lst)})
    
#     # Обработка POST-запросов:
#     def post(self, request):
#         post_new = Women.objects.create(
#             title=request.data['title'],
#             content=request.data['content'],
#             cat_id=request.data['cat_id'],
#         ) 
#         return Response({'post': model_to_dict(post_new)})

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


# Урок 4: Введение в сериализацию
class WomenAPIView(APIView):
    # Обработка GET-запросов:
    def get(self, request):
        w = Women.objects.all()
        return Response({'posts': WomenSerializer(w, many=True).data})
    
    # Обработка POST-запросов:
    def post(self, request):
        # Проверяем корректность данных:
        serializers = WomenSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)

        post_new = Women.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id'],
        ) 
        return Response({'post': WomenSerializer(post_new).data})