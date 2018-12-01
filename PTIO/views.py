from django.shortcuts import render
from django.http.response import Http404
from PTIO.models.profile import ParentProfile, TeacherProfile, StudentProfile
from PTIO.models.meeting import TeacherClass, MeetingTimeslot


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

def student(request):
    return render(request, 'PTIO/student.html', {})
