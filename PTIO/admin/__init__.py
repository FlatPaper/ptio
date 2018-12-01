from django.contrib import admin

from PTIO.admin.profile import ProfileAdmin
from PTIO.models import Profile

admin.site.register(Profile, ProfileAdmin)
