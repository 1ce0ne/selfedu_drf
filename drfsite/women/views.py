from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Women, Category
from .serializers import WomenSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from rest_framework.authentication import TokenAuthentication


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
# class WomenAPIView(APIView):
#     # Обработка GET-запросов:
#     def get(self, request):
#         w = Women.objects.all()
#         return Response({'posts': WomenSerializer(w, many=True).data})
    
#     # Обработка POST-запросов:
#     def post(self, request):
#         # Проверяем корректность данных:
#         serializers = WomenSerializer(data=request.data)
#         serializers.is_valid(raise_exception=True)

#         post_new = Women.objects.create(
#             title=request.data['title'],
#             content=request.data['content'],
#             cat_id=request.data['cat_id'],
#         ) 
#         return Response({'post': WomenSerializer(post_new).data})
    

# Урок 5: Методы save(), create() и update()
# class WomenAPIView(APIView):
#     # Обработка GET-запросов:
#     def get(self, request):
#         w = Women.objects.all()
#         return Response({'posts': WomenSerializer(w, many=True).data})
    
#     # Обработка POST-запросов:
#     def post(self, request):
#         # Проверяем корректность данных:
#         serializers = WomenSerializer(data=request.data)
#         serializers.is_valid(raise_exception=True)
#         serializers.save()

#         return Response({'post': serializers.data})
    
#     # Обработка PUT-запросов:
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
        
#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object doesn't exists"})
        
#         serializer = WomenSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
    
#     # Обработка DELETE-запросов:
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
        
#         try:
#             instance = Women.objects.get(pk=pk)
#             deleted_title = str(instance.title)
#             instance.delete()
#         except:
#             return Response({"error": "Object doesn't exists"})
        
#         return Response({"post": f"delete post {str(pk)} : {deleted_title}"})
    


# Урок 6: Класс ModelSerializer и представление ListCreateAPIView
# class WomenAPIList(generics.ListCreateAPIView):
#     """
#     GET и CREATE
#     """
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


# Урок 7: Представления UpdateAPIView и RetrieveUpdateDestroyAPIView
# class WomenAPIUpdate(generics.UpdateAPIView):
#     """
#     UPDATE
#     """
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

# class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     """
#     CRUD для отдельной записи
#     """
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


# Урок 8: Viewsets и ModelViewSet
# class WomenViewSet(viewsets.ModelViewSet):
#     """
#     CRUD
#     """
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

# class WomenViewSet(viewsets.ReadOnlyModelViewSet):
#     """
#     READ
#     """
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


# Урок 9: Роутеры: SipleRouter и DefaultRouter
# class WomenViewSet(viewsets.ModelViewSet):
#     #queryset = Women.objects.all()
#     serializer_class = WomenSerializer
 
#     # Переопределяем queryset
#     def get_queryset(self):
#         pk = self.kwargs.get("pk")

#         if not pk:
#             return Women.objects.all()[:3]
        
#         return Women.objects.filter(pk=pk)

    
#     # Добавляем новые маршруты
#     @action(methods=['get'], detail=True)
#     def category(self, request, pk=None):
#         cats = Category.objects.get(pk=Women.objects.get(pk=pk).cat_id)
#         return Response({'cats': cats.name})
    

# Урок 10: Ограничения доступа (permissions) 
# class WomenAPIList(generics.ListCreateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#     permission_classes = (IsAuthenticatedOrReadOnly, )

# class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#     permission_classes = (IsOwnerOrReadOnly, )

# class WomenAPIDestroy(generics.RetrieveDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#     permission_classes = (IsAdminOrReadOnly, )


# Урок 12: Аутентификация по токенам. Пакет Djoser
class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticated, )
    # Можем разграничивать данные по способу авторизации
    #authentication_classes = (TokenAuthentication, )

class WomenAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAdminOrReadOnly, )