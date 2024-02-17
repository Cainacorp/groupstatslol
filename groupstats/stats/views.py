from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import *
from rest_framework import status
from .models import *


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializerBasic

    def create(self, request, *args, **kwargs):
        try:
            User.objects.create_user(username=request.data.get('username'), password=request.data.get(
                'username'), first_name=request.data.get('first_name'), last_name=request.data.get('last_name'))
            return Response('Usuario creado!', status=status.HTTP_201_CREATED)
        except Exception as e:
            message = e.args[1] or 'Error al crear usuario'
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

class SummonerViewSet(ModelViewSet):
    queryset = Summoner.objects.all()
    serializer_class = SummonerSerializer

class SummonerGroupViewSet(ModelViewSet):
    queryset = SummonerGroup.objects.all()
    serializer_class = SummonerGroupSerializer

class RoleViewSet(ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class PlayWith(ModelViewSet):
    queryset = PlayWith.objects.all()
    serializer_class = PlayWithSerializer

# TODO agregar endpoint (APIView) para scrapear
