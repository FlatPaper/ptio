from django.contrib import admin

from PTIO.admin.profile import ProfileAdmin
from PTIO.models import Profile

from PTIO.admin.meeting import MeetingTimeslotAdmin
from PTIO.models import MeetingTimeslot

from PTIO.admin.profile import StudentProfileAdmin, ParentProfileAdmin
from PTIO.models import StudentProfile, ParentProfile

admin.site.register(MeetingTimeslot, MeetingTimeslotAdmin)
admin.site.register(StudentProfile, StudentProfileAdmin)
admin.site.register(ParentProfile, ParentProfileAdmin)

admin.site.register(Profile, ProfileAdmin)
