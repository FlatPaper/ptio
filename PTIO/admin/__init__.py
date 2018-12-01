from django.contrib import admin

from PTIO.admin.profile import StudentProfileAdmin, ParentProfileAdmin, TeacherProfileAdmin
from PTIO.admin.meeting import MeetingTimeslotAdmin, TeacherClassAdmin, UsedTimeSlotAdmin
from PTIO.models import StudentProfile, ParentProfile, TeacherProfile, MeetingTimeslot, TeacherClass, UsedTimeSlot

admin.site.register(MeetingTimeslot, MeetingTimeslotAdmin)
admin.site.register(TeacherClass, TeacherClassAdmin)
admin.site.register(UsedTimeSlot, UsedTimeSlotAdmin)

admin.site.register(StudentProfile, StudentProfileAdmin)
admin.site.register(ParentProfile, ParentProfileAdmin)
admin.site.register(TeacherProfile, TeacherProfileAdmin)
