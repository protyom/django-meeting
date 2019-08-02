from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import EmailMessage
from meetings.models import Meeting
from users.models import CustomUser

from django.contrib.gis.geoip2 import GeoIP2
from ipware import get_client_ip

@api_view()
def null_view(request):
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view()
def complete_view(request):
    return Response("Email account is activated")


@api_view()
def email_test(request):
    g = GeoIP2()
    ip = get_client_ip(request)
    return Response("User IP checK: " + g.country("194.158.218.46")["country_code"])


@api_view(["POST"])
def set_name(request):
    pass


@api_view(["PUT"])
def change_meeting(request, pk):
    meeting = Meeting.objects.get(pk=pk)
    result = {"students_count": meeting.students_count,
              "available": meeting.students_count - meeting.students.count()}
    if not request.user.is_authenticated:
        result["details"] = "You have to authenticate"
        return Response(result)
    current_user = CustomUser.objects.get(username=request.user.username)
    if current_user.role == current_user.TEACHER:
        result["details"] = "You are not student!"
        return Response(result)
    if current_user.country != meeting.teacher.country:
        result["details"] = "You are not from " + meeting.teacher.country.name + "!"
        return Response(result)
    if current_user in meeting.students.all():
        result["details"] = "You have left the meeting"
        meeting.students.remove(current_user)
        result["students_count"] = meeting.students_count
        result["available"] = meeting.students_count - meeting.students.count()
        return Response(result)
    elif current_user not in meeting.students.all() and meeting.students.count() < meeting.students_count:
        meeting.students.add(current_user)
        result["students_count"] = meeting.students_count
        result["available"] = meeting.students_count - meeting.students.count()
        result["details"] = "You have joined the meeting"
        return Response(result)
    else:
        result["details"] = "Meeting is full"
        return Response(result)
