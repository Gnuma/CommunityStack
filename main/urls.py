from django.urls import path
from .views import Prova

urlpatterns = [
    path('prova/', Prova.as_view())
]