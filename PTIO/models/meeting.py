from django.db import models
from .profile import Profile


class MeetingTimeslot(models.Model):
    teacher = models.ForeignKey(Profile, on_delete=models.CASCADE)
    start_time = models.DateTimeField(verbose_name='Start Time')
    end_time = models.DateTimeField(verbose_name='End Time', validators=[])
    start_display_time = models.DateTimeField(verbose_name='Start Display Time')

    def __str__(self):
        return 'Meeting by %s from %s to %s' % (self.teacher, self.start_time, self.end_time)
