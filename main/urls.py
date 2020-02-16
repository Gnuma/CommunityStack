from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CategoryHandler, TopicHandler, TutorialHandler

router = DefaultRouter()
router.register('categories', CategoryHandler)
router.register('topics', TopicHandler)
router.register('tutorials', TutorialHandler)

urlpatterns = [
]

urlpatterns += router.urls
