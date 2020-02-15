from django.urls import path
from .views import Prova

urlpatterns = [
    path('/', Prova.as_view())
]