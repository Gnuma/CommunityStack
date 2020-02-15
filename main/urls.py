from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CategoryHandler

router = DefaultRouter()
router.register('categories', CategoryHandler)

urlpatterns = [
]

urlpatterns += router.urls