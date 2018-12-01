from django.contrib import admin

from PTIO.admin.meeting import MeetingTimeslotAdmin, TeacherClassAdmin
from PTIO.models import MeetingTimeslot, TeacherClass

from PTIO.admin.profile import StudentProfileAdmin, ParentProfileAdmin
from PTIO.models import StudentProfile, ParentProfile

admin.site.register(MeetingTimeslot, MeetingTimeslotAdmin)
admin.site.register(TeacherClass, TeacherClassAdmin)

admin.site.register(StudentProfile, StudentProfileAdmin)
admin.site.register(ParentProfile, ParentProfileAdmin)
