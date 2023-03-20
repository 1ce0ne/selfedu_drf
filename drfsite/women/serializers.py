from rest_framework import serializers
from .models import Women

# Урок 2: Пример простого сериализатора
class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = ('title', 'cat_id') 