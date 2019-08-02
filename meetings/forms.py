from django import forms
from .models import Meeting
from users.models import CustomUser
from django.db.models import Q
from django.core.exceptions import ValidationError


class MeetingForm(forms.ModelForm):

    class Meta:
        model = Meeting
        fields = ('name', 'date', 'teacher', 'students_count', 'students', 'details')

    def clean(self):
        students_count = int(self.cleaned_data.get('students_count'))
        students = self.cleaned_data.get('students')
        teacher = self.cleaned_data.get('teacher')
        if students:
            if students.count() != students_count:
                raise ValidationError("You can't add more than " + str(students_count) + " students!")
            for student in students:
                if student.country != teacher.country:
                    raise ValidationError("Student " + student.username + " is not from " + teacher.country.name + "!")
