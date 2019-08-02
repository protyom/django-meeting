from django.db import models
from django.core.exceptions import ValidationError
from django_countries.serializers import CountryFieldMixin
from django.utils import timezone

from users.models import CustomUser


class Meeting(models.Model):
    name = models.CharField(max_length=30, blank=False, default="")
    date = models.DateTimeField(blank=False, default=timezone.now)
    teacher = models.ForeignKey(CustomUser, related_name="teacher", limit_choices_to={'role': CustomUser.TEACHER},
                                blank=False,
                                on_delete=models.CASCADE,
                                default=1)
    details = models.TextField()
    students_count = models.IntegerField(blank=False, default=1)
    students = models.ManyToManyField(CustomUser, limit_choices_to={'role': CustomUser.STUDENT},
                                      related_name="user_meetings", blank=True)

    def __str__(self):
        return self.name
