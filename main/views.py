from rest_framework.views import APIView
from django.http import JsonResponse

class Prova(APIView):

    def get(self, request, format = None):
        return JsonResponse({'ciao':'ciao'})