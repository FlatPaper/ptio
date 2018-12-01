from django.contrib import admin

from PTIO.admin.profile import StudentProfileAdmin, ParentProfileAdmin, TeacherProfileAdmin
from PTIO.models import StudentProfile, ParentProfile, TeacherProfile

admin.site.register(StudentProfile, StudentProfileAdmin)
admin.site.register(ParentProfile, ParentProfileAdmin)
admin.site.register(TeacherProfile, TeacherProfileAdmin)
