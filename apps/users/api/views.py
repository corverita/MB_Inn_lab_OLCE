from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.exceptions import NotFound
from rest_framework.decorators import action

from django_filters.rest_framework import DjangoFilterBackend
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from ..models import *
from .pagination import Paginador
from .serializers import *
from .utils import *

class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['email', 'nombre', 'apellido_paterno', 'apellido_materno', 'edad', 'telefono', 'is_staff', 'is_active']
    ordering_fields = ['email', 'nombre', 'apellido_paterno', 'apellido_materno', 'edad', 'telefono', 'is_staff', 'is_active']
    filter_fields = ['email', 'nombre', 'apellido_paterno', 'apellido_materno', 'edad', 'telefono', 'is_staff', 'is_active']
    pagination_class = Paginador

    def get_serializer_class(self):
        if self.action == 'create':
            return CrearCustomUserSerializer
        if self.action == 'update':
            return ActualizarCustomUserSerializer
        if self.action == 'destroy':
            return EliminarCustomUserSerializer
        if self.action == 'usuarios_ordenados_edad':
            return OrdenarUsuariosEdad
        return CustomUserSerializer
    
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('ascendant', openapi.IN_QUERY, description="Ascendente", type=openapi.TYPE_BOOLEAN, default=False, required=True),
        ]
    )
    @action(detail=False, methods=['get'])
    def usuarios_ordenados_edad(self, request):
        queryset = self.get_queryset()
        ascendant = request.query_params.get('ascendant')
        queryset = QuerysetSorter.bubble_sort(queryset, "edad", ascendant=ascendant)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = CustomUserSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = CustomUserSerializer(queryset, many=True)
        return Response(serializer.data)
    

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('ascendant', openapi.IN_QUERY, description="Ascendente", type=openapi.TYPE_BOOLEAN, default=False, required=True),
        ]
    )
    @action(detail=False, methods=['get'])
    def usuarios_ordenados_apellido(self, request):
        queryset = self.get_queryset()
        ascendant = request.query_params.get('ascendant')
        queryset = QuerysetSorter.bubble_sort(queryset, "apellido_paterno", ascendant=ascendant)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = CustomUserSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = CustomUserSerializer(queryset, many=True)
        return Response(serializer.data)