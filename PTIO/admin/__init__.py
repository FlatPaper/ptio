from django.contrib import admin

from PTIO.admin.profile import ProfileAdmin
from PTIO.models import Profile
from PTIO.admin.meeting import MeetingTimeslotAdmin
from PTIO.models import MeetingTimeslot

admin.site.register(Profile, ProfileAdmin)
admin.site.register(MeetingTimeslot, MeetingTimeslotAdmin)