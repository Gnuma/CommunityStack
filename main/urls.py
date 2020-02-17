from django.urls import path
from rest_framework.routers import DefaultRouter
from .utils.custom_routers import RetrieveByCategoryRouter
from .views import CategoryHandler, TopicHandler

router = DefaultRouter()
router.register('categories', CategoryHandler)
category = RetrieveByCategoryRouter()
category.register('topics', TopicHandler)

urlpatterns = [
]

urlpatterns += router.urls
urlpatterns += category.urls