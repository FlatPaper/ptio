from django.db import models
from django.core.validators import RegexValidator
from .profile import TeacherProfile, StudentProfile

SUBJECT_VALIDATORS = [RegexValidator(regex='^[a-zA-Z ]+$', message='Subject can only contain letters and spaces')]


class TeacherClass(models.Model):
    teacher = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200, validators=SUBJECT_VALIDATORS)
    students = models.ManyToManyField(StudentProfile)

    def __str__(self):
        return '%s\'s %s class' % (self.teacher, self.subject)


class MeetingTimeslot(models.Model):
    teacher_class = models.ForeignKey(TeacherClass, on_delete=models.CASCADE)
    start_time = models.DateTimeField(verbose_name='Start Time')
    end_time = models.DateTimeField(verbose_name='End Time', validators=[])
    start_display_time = models.DateTimeField(verbose_name='Start Display Time')

    def __str__(self):
        return 'Meeting by %s from %s to %s' % (self.teacher_class, self.start_time, self.end_time)
