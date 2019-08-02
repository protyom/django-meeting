from rest_framework import serializers
from .models import Meeting


class MeetingSerializer(serializers.ModelSerializer):
    teacher_username = serializers.CharField(source='teacher.username')
    teacher_name = serializers.CharField(source='teacher.first_name')
    teacher_country = serializers.CharField(source='teacher.country.name')

    class Meta:
        model = Meeting
        fields = ('pk', 'name', 'teacher', 'teacher_username', 'teacher_name', 'teacher_country', 'date', 'details',
                  'students_count', 'students', )
