from django.urls import include, path, re_path

from .views import ListMeetings, ListUserFinishedMeetings, ListUserFutureMeetings


urlpatterns = [
    path('', ListMeetings.as_view()),
    path('finished/', ListUserFinishedMeetings.as_view()),
    path('future/', ListUserFutureMeetings.as_view()),
]
