from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import BasePermission, IsAdminUser

from .models import CustomUser
from .serializers import UserSerializer, UserEditSerializer


class UserListView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class IsOwnerUser(BasePermission):
    def has_permission(self, request, view):
        if request.user.pk == view.kwargs['pk'] or request.user.is_superuser:
            return True

        return False


class UserRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    lookup_field = 'pk'
    permission_classes = [IsOwnerUser]
    serializer_class = UserEditSerializer
    queryset = CustomUser.objects.all()



