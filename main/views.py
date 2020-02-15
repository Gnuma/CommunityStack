from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from django.http import JsonResponse
from .serializers import CategorySerializer
from .models import Category

class CategoryHandler(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
