from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from .serializers import MeetingSerializer
from .models import Meeting
from django.utils import timezone
from users.models import CustomUser


class ListMeetings(generics.ListAPIView):
    serializer_class = MeetingSerializer
    queryset = Meeting.objects.filter(date__gte=timezone.now())


class ListUserFinishedMeetings(generics.ListAPIView):
    serializer_class = MeetingSerializer
    pagination_class = None

    def get_queryset(self):
        user = CustomUser.objects.get(id=self.request.user.id)
        return user.user_meetings.filter(date__lte=timezone.now())


class ListUserFutureMeetings(generics.ListAPIView):
    serializer_class = MeetingSerializer
    pagination_class = None

    def get_queryset(self):
        user = CustomUser.objects.get(id=self.request.user.id)
        return user.user_meetings.filter(date__gte=timezone.now())


