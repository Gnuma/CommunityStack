from rest_framework.serializers import ModelSerializer
from .models import Category, Topic

class CategorySerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Category


class TopicSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Topic