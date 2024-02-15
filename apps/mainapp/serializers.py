from rest_framework import serializers
from .models import Category, News


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
        
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
        real_only_fields = ['created_at', 'updated_at', 'view']  # Поля которые нельзя изменять
        extra_kwargs = {
            'title': {'max_length': 200},
            'text': {'max_length': 5000},
        }