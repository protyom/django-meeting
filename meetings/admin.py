from django.contrib import admin
from .models import Meeting
from .forms import MeetingForm


class MeetingAdmin(admin.ModelAdmin):
    form = MeetingForm


admin.site.register(Meeting, MeetingAdmin)
