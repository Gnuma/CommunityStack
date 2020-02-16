from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from django.http import JsonResponse
from .serializers import CategorySerializer, TopicSerializer
from .models import Category, Topic


class CategoryHandler(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class TopicHandler(ModelViewSet):
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()
    lookup_field = "category"
