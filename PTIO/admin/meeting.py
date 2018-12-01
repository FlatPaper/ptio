from django.contrib import admin
from django.forms import ModelForm
from django.utils.translation import ugettext, ugettext_lazy as _


class MeetingTimeslotAdmin(admin.ModelAdmin):
    list_display = ('teacher_class', 'start_time', 'end_time')
    list_display_links = ('teacher_class',)
    search_fields = ('class', 'subject')
    list_per_page = 25


class TeacherClassAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'subject')
    list_display_links = ('teacher',)
    search_fields = ('teacher__user_name', 'subject')
    list_per_page = 25
