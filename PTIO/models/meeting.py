from django.db import models
from django.core.validators import RegexValidator
from .profile import ParentProfile


class MeetingTimeslot(models.Model):
    teacher = models.ForeignKey(ParentProfile, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200, validators=[RegexValidator(regex='^[a-zA-Z ]+$', message='Subject can only contain letters and spaces')])
    start_time = models.DateTimeField(verbose_name='Start Time')
    end_time = models.DateTimeField(verbose_name='End Time', validators=[])
    start_display_time = models.DateTimeField(verbose_name='Start Display Time')

    def __str__(self):
        return 'Meeting by %s from %s to %s' % (self.teacher, self.start_time, self.end_time)


class TeacherClass(models.Model):
    teacher = models.