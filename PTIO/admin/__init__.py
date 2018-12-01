from django.contrib import admin

from PTIO.admin.profile import StudentProfileAdmin, ParentProfileAdmin, TeacherProfileAdmin
from PTIO.admin.meeting import MeetingTimeslotAdmin, TeacherClassAdmin
from PTIO.models import StudentProfile, ParentProfile, TeacherProfile, MeetingTimeslot, TeacherClass

admin.site.register(MeetingTimeslot, MeetingTimeslotAdmin)
admin.site.register(TeacherClass, TeacherClassAdmin)

admin.site.register(StudentProfile, StudentProfileAdmin)
admin.site.register(ParentProfile, ParentProfileAdmin)
admin.site.register(TeacherProfile, TeacherProfileAdmin)
