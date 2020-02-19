from django.http import JsonResponse
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from .serializers import UserSerializer
from ..models import User


class UserHandler(GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail = False, methods = ['get'])
    def top_contributors(self, request):
        top_contributors = self.get_queryset().order_by('-contributions')[:5]
        response = self.get_serializer_class()(top_contributors, many = True).data

        return JsonResponse(response, status = status.HTTP_200_OK, safe = False)
    
    @action(detail = False, methods = ['get'])
    def last_contributors(self, request):
        """
        Verificare come si comporta con i last_contribution = None.
        """
        last_contributors = self.get_queryset().order_by('-last_contribution')
        response = self.get_serializer_class()(last_contributors, many = True).data

        return JsonResponse(response, status = status.HTTP_200_OK, safe = False)
        