# Generated by Django 2.1.1 on 2018-12-01 20:26

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MeetingTimeslot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(verbose_name='Start Time')),
                ('end_time', models.DateTimeField(verbose_name='End Time')),
                ('start_display_time', models.DateTimeField(verbose_name='Start Display Time')),
            ],
        ),
        migrations.CreateModel(
            name='ParentProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name_parent_1', models.CharField(blank=True, max_length=200, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z]+$', 'First name must be made of characters only.')], verbose_name='parent 1 first name')),
                ('second_name_parent_1', models.CharField(blank=True, max_length=200, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z]+$', 'Second name must be made of characters only.')], verbose_name='parent 1 second name')),
                ('first_name_parent_2', models.CharField(blank=True, max_length=200, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z]+$', 'First name must be made of characters only.')], verbose_name='parent 2 first name')),
                ('second_name_parent_2', models.CharField(blank=True, max_length=200, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z]+$', 'Second name must be made of characters only.')], verbose_name='parent 2 second name')),
                ('user_name', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=200, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z]+$', 'First name must be made of characters only.')])),
                ('last_name', models.CharField(blank=True, max_length=200, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z]+$', 'First name must be made of characters only.')])),
                ('parent_account_host', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='PTIO.ParentProfile', verbose_name='parents')),
            ],
            options={
                'verbose_name': 'student',
                'verbose_name_plural': 'students',
                'permissions': (('edit_own_children', 'Edit own children'),),
            },
        ),
        migrations.CreateModel(
            name='TeacherClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(message='Subject can only contain letters and spaces', regex='^[a-zA-Z ]+$')])),
                ('students', models.ManyToManyField(to='PTIO.StudentProfile')),
            ],
        ),
        migrations.CreateModel(
            name='TeacherProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=200, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z]+$', 'First name must be made of characters only.')])),
                ('last_name', models.CharField(blank=True, max_length=200, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z]+$', 'Last name must be made of characters only.')])),
                ('user_name', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='teacherclass',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PTIO.TeacherProfile'),
        ),
        migrations.AddField(
            model_name='meetingtimeslot',
            name='teacher_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PTIO.TeacherClass'),
        ),
    ]
