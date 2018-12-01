from django.contrib import admin
from django.forms import ModelForm
from django.utils.translation import ugettext, ugettext_lazy as _

from PTIO.models import Profile

class ProfileAdmin(admin.ModelAdmin):
    fields = ('user_name', 'display_rank', 'first_name', 'last_name')
