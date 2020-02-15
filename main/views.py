from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.http import JsonResponse

class Prova(APIView):

    permission_classes = [AllowAny, ]

    def get(self, request, format = None):
        return JsonResponse({'ciao':'ciao'})