from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from django_countries.serializers import CountryFieldMixin


class CustomUser(AbstractUser):
    STUDENT = "STD"
    TEACHER = "TCH"
    ROLES = [
        (STUDENT, "Student"),
        (TEACHER, "Teacher"),
    ]
    role = models.CharField(max_length=3, choices=ROLES)
    country = CountryField()

    def __str__(self):
        return self.username
