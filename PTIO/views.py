from django.shortcuts import render
from django.urls import reverse
from django.http.response import Http404, HttpResponseRedirect
from PTIO.models.profile import ParentProfile, TeacherProfile, StudentProfile
from PTIO.models.meeting import TeacherClass, MeetingTimeslot, UsedTimeSlot
import datetime
import pytz


# Create your views here.

def index(request):
    students = StudentProfile.objects.all()
    parents = ParentProfile.objects.all()
    teachers = TeacherProfile.objects.all()
    classes = TeacherClass.objects.all()

    return render(request, 'PTIO/index.html', {'students': students, 'parents': parents, 'teachers': teachers,
                                               'classes': classes})


def parent(request, parent_id):
    try:
        parent_obj = ParentProfile.objects.get(pk=parent_id)
        children = StudentProfile.objects.filter(parent_account_host__pk=parent_id).all()
        children_ids = map(lambda child: child.id, children)
        classes = []
        meetings = []

        for curr_class in TeacherClass.objects.all():
            relevant = False

            for student in curr_class.students.all():
                if student.id in children_ids:
                    relevant = True
                    break

            if relevant:
                classes.append(curr_class)

        for meeting in MeetingTimeslot.objects.all():
            for curr_class in classes:
                if meeting.teacher_class.id == curr_class.id:
                    meetings.append((curr_class, meeting))
                    break

        return render(request, 'PTIO/parent.html', {'parent_id': parent_id, 'parent_obj': parent_obj,
                                                    'children': children, 'meetings': meetings})
    except ParentProfile.DoesNotExist:
        raise Http404('Invalid parent id!')


def teacher(request, teacher_id):
    try:
        teacher_obj = TeacherProfile.objects.get(pk=teacher_id)
        classes = []
        for class_obj in TeacherClass.objects.filter(teacher__pk=teacher_id).all():
            classes.append((class_obj, class_obj.students.all()))

        slots = MeetingTimeslot.objects.filter(teacher_class__teacher__pk=teacher_id)

        return render(request, 'PTIO/teacher.html', {'teacher_id': teacher_id, 'teacher_obj': teacher_obj,
                                                     'classes': classes, 'slots': slots})
    except TeacherProfile.DoesNotExist:
        raise Http404('Invalid teacher id!')


def register_slot(request, parent_id, slot_id):
    meeting = MeetingTimeslot.objects.get(pk=slot_id)
    parent = ParentProfile.objects.get(pk=parent_id)
    already_used = UsedTimeSlot.objects.filter(parent_slot__pk=slot_id)

    return render(request, 'PTIO/register_slot.html', {'slot_obj': meeting, 'parent_obj': parent,
                                                       'used': already_used})


def str_to_datetime(date_string):
    spl = date_string.split('T')
    y, m, d = map(int, spl[0].split('-'))
    h, m = map(int, spl[1].split(':'))
    return datetime.datetime(y, m, d, h, m, 0, tzinfo=pytz.UTC)


def register_slot_post(request):
    parent = ParentProfile.objects.get(pk=request.POST['parentid'])
    slot = MeetingTimeslot.objects.get(pk=request.POST['slotid'])
    usedslots = UsedTimeSlot.objects.get(pk=slot.id)

    curstart = str_to_datetime(request.POST['start-time'])
    curend = str_to_datetime(request.POST['end-time'])

    if curstart < slot.start_time or curend > slot.end_time:
        return render(request, 'PTIO/register_slot.html', {'err': 'Chosen time slot not within parent slot bounds!'})

    works = True
    for usedslot in usedslots:
        if curend > usedslot.start_time or curstart < usedslot.end_time:
            works = False
            break

    if works:
        return render(request, 'PTIO/register_slot.html', {'err': 'Time slot submitted!'})
    else:
        return render(request, 'PTIO/register_slot.html', {'err': 'Chosen time slot is already taken!'})


def student(request):
    return render(request, 'PTIO/student.html', {})
