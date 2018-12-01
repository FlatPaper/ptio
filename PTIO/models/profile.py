from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.utils.functional import cached_property

class TeacherProfile(models.Model):
    user_name = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=200, blank=True, null=True,
        validators=[RegexValidator('^[a-zA-Z]+$', _('First name must be made of characters only.'))])
    last_name = models.CharField(max_length=200, blank=True, null=True,
        validators=[RegexValidator('^[a-zA-Z]+$', _('Last name must be made of characters only.'))])

    def __str__(self):
        if self.first_name and self.last_name:
            return str(self.first_name + " " + self.last_name)
        return self.user.user_name

class ParentProfile(models.Model):
    user_name = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name_parent_1 = models.CharField(max_length=200, blank=True, null=True, verbose_name=_('parent 1 first name'),
        validators=[RegexValidator('^[a-zA-Z]+$', _('First name must be made of characters only.'))])
    second_name_parent_1 = models.CharField(max_length=200, blank=True, null=True, verbose_name=_('parent 1 second name'),
        validators=[RegexValidator('^[a-zA-Z]+$', _('Second name must be made of characters only.'))])
    first_name_parent_2 = models.CharField(max_length=200, blank=True, null=True, verbose_name=_('parent 2 first name'),
        validators=[RegexValidator('^[a-zA-Z]+$', _('First name must be made of characters only.'))])
    second_name_parent_2 = models.CharField(max_length=200, blank=True, null=True, verbose_name=_('parent 2 second name'),
        validators=[RegexValidator('^[a-zA-Z]+$', _('Second name must be made of characters only.'))])

    def __str__(self):
        if self.user_name:
            return str(self.user_name)
        return self.user.user_name

class StudentProfile(models.Model):
    parent_account_host = models.ForeignKey(ParentProfile, on_delete=models.PROTECT, verbose_name=_('parents'))
    first_name = models.CharField(max_length=200, blank=True, null=True,
        validators=[RegexValidator('^[a-zA-Z]+$', _('First name must be made of characters only.'))])
    last_name = models.CharField(max_length=200, blank=True, null=True,
        validators=[RegexValidator('^[a-zA-Z]+$', _('Last name must be made of characters only.'))])

    def is_accessible_by(self, user):
        if user.has_perm('PTIO.edit_own_children'):
            return True
        return False

    def __str__(self):
        if self.first_name and self.last_name:
            return str(self.first_name + " " + self.last_name)
        return self.user.user_name

    def is_editor(self, profile):
        return (self.parent_account_host.filter(id=ParentProfile.id)).exists()

    @cached_property
    def parent_id(self):
        return self.parent_account_host.values_list('id', flat=True)

    class Meta:
        permissions = (
            ('edit_own_children', 'Edit own children'),
            ('edit_all_children', 'Edit all children'),
        )
        verbose_name = _('student')
        verbose_name_plural = _('students')
