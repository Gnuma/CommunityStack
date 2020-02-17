from rest_framework.serializers import ModelSerializer
from .models import Category, Topic, Tutorial


class CategorySerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Category


class TopicSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Topic


class TutorialSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Tutorial
