from django.shortcuts import render
from rest_framework import generics
from .models import Women
from .serializers import WomenSerializer

# Урок 2: Пример простого представления
class WomenAPIView(generics.ListAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer