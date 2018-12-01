from django.shortcuts import render
from django.http.response import Http404
from PTIO.models.profile import ParentProfile, TeacherProfile, StudentProfile
from PTIO.models.meeting import TeacherClass


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
        children = StudentProfile.objects.filter(parent_account_host__pk=parent_id)
        meetings = []

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

        return render(request, 'PTIO/teacher.html', {'teacher_id': teacher_id, 'teacher_obj': teacher_obj,
                                                     'classes': classes})
    except TeacherProfile.DoesNotExist:
        raise Http404('Invalid teacher id!')


def student(request):
    return render(request, 'PTIO/student.html', {})
