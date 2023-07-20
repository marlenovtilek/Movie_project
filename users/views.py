from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as rest_filters
from rest_framework import filters
from rest_framework.decorators import action 
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser


from users.models import User
from users.serializers import UserSerializer
from users.filters import UserFilter
from users.permissions import IsAdminOrReadOnly


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]
    filter_backends = (rest_filters.DjangoFilterBackend, filters.SearchFilter)
    filterset_class = UserFilter
    search_fields = ['username', 'email']


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        
        refresh = RefreshToken.for_user(serializer.instance)
        response_data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)