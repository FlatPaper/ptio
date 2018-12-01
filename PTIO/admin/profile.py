from django.contrib import admin

class StudentProfileAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name')

class ParentProfileAdmin(admin.ModelAdmin):
    fields = ('user_name', 'first_name_parent_1', 'second_name_parent_1', 'first_name_parent_2', 'second_name_parent_2')
