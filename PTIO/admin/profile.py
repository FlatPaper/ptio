from django.contrib import admin
from django.db.models import Q

from PTIO.models import StudentProfile, ParentProfile

class StudentProfileAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'parent_account_host')

    def get_queryset(self, request):
        queryset = StudentProfile.objects.all()
        if request.user.has_perm('judge.edit_all_children'):
            return queryset

        access = Q()
        if request.user.has_perm('PTIO.edit_own_children'):
            access |= Q(parent_account_host__id=request.user.id)
        return queryset.filter(access).distinct() if access else queryset.none()

class ParentProfileAdmin(admin.ModelAdmin):
    fields = ('user_name', 'first_name_parent_1', 'second_name_parent_1', 'first_name_parent_2', 'second_name_parent_2')
    list_display = ('user_name', 'first_name_parent_1', 'second_name_parent_1', 'first_name_parent_2', 'second_name_parent_2')
    list_display_links = ('user_name', )


class TeacherProfileAdmin(admin.ModelAdmin):
    fields = ('user_name', 'first_name', 'last_name')
