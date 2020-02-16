from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CategoryHandler, TopicHandler

router = DefaultRouter()
router.register('categories', CategoryHandler)
router.register('topics', TopicHandler)

urlpatterns = [
]

urlpatterns += router.urls