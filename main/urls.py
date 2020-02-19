from django.urls import path
from rest_framework.routers import DefaultRouter
from .utils.custom_routers import RetrieveByCategoryRouter
from .views import CategoryHandler, TopicHandler
from .user_management import *

router = DefaultRouter()
router.register('categories', CategoryHandler)
router.register('users', UserHandler)
category = RetrieveByCategoryRouter()
category.register('topics', TopicHandler)

urlpatterns = [
]

urlpatterns += router.urls
urlpatterns += category.urls
