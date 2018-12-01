from django.contrib import admin

from PTIO.admin.profile import StudentProfileAdmin, ParentProfileAdmin
from PTIO.models import StudentProfile, ParentProfile

admin.site.register(StudentProfile, StudentProfileAdmin)
admin.site.register(ParentProfile, ParentProfileAdmin)
