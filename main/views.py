from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from django.http import JsonResponse
from .serializers import CategorySerializer, TopicSerializer, TutorialSerializer
from .models import Category, Topic, Tutorial


class CategoryHandler(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class TopicHandler(ModelViewSet):
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()

    def list(self, request, *args, **kwargs):
        self.queryset = Topic.objects.filter(category=kwargs['pk'])
        return super().list(self, request, *args, **kwargs)


class TutorialHandler(ModelViewSet):
    serializer_class = TutorialSerializer
    queryset = Topic.objects.all()

    def list(self, request, *args, **kwargs):
        self.queryset = Tutorial.objects.filter(topic=kwargs['pk'])
        return super().list(self, request, *args, **kwargs)
