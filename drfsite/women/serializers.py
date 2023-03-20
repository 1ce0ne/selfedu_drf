from rest_framework import serializers
from .models import Women
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser

# Урок 2: Пример простого сериализатора
# class WomenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Women
#         fields = ('title', 'cat_id') 


# Урок 3: Введение в сериализацию
# class WomenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content

# class WomenSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()

# def encode():
#     """
#     Инструкция:
#         1. python3 manage.py shell
#         2. from women.serializers import encode
#         3. encode()
#     """
#     model = WomenModel('Genevieve Richter', 'Content: TheVzryv')
#     model_sr = WomenSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)

# def decode():
#     stream = io.BytesIO(b'{"title":"Genevieve Richter","content":"Content: TheVzryv"}')
#     data = JSONParser().parse(stream)
#     serializers = WomenSerializer(data=data)
#     serializers.is_valid()
#     print(serializers.validated_data)

class WomenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()