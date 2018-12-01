from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

class Profile(models.Model):
    user_name = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=200, blank=True, null=True,
        validators=[RegexValidator('^[a-zA-Z]+$', _('First name must be made of characters only.'))])
    last_name = models.CharField(max_length=200, blank=True, null=True,
        validators=[RegexValidator('^[a-zA-Z]+$', _('First name must be made of characters only.'))])

    def __str__(self):
        if self.user_name:
            return str(self.user_name)
        return self.user.user_name
