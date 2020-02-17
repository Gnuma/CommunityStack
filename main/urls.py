from django.urls import path
from rest_framework.routers import DefaultRouter
from .utils.custom_routers import RetrieveByCategoryRouter, RetrieveByTopicRouter
from .views import CategoryHandler, TopicHandler, TutorialHandler

router = DefaultRouter()
router.register('categories', CategoryHandler)
category = RetrieveByCategoryRouter()
category.register('topics', TopicHandler)
topic = RetrieveByTopicRouter()
topic.register('tutorials', TutorialHandler)

urlpatterns = [
]

urlpatterns += router.urls
urlpatterns += category.urls
urlpatterns += topic.urls
