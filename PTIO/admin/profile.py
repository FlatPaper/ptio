from django.contrib import admin

class StudentProfileAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'parent_account_host')

class ParentProfileAdmin(admin.ModelAdmin):
    fields = ('user_name', 'first_name_parent_1', 'second_name_parent_1', 'first_name_parent_2', 'second_name_parent_2')
    list_display = ('user_name', 'first_name_parent_1', 'second_name_parent_1', 'first_name_parent_2', 'second_name_parent_2')
    list_display_links = ('user_name', )

class TeacherProfileAdmin(admin.ModelAdmin):
    fields = ('user_name', 'first_name', 'last_name')
