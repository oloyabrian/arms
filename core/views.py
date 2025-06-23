from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import Student, Grade, Subject, Term, Teacher, Parent, ReportComment

from .forms import *
from .models import *
from django.db.models import Avg
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'chart.html', {})

# Simple API view returning dummy data (you can remove if not needed)
def get_data(request, *args, **kwargs):
    data = {
        'sales': 100,
        'customers': 10
    }
    return JsonResponse(data)

# API endpoint returning counts of different models (can be used by JS frontend)
class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        data = {
            'Users': User.objects.count(),
            'Students': Student.objects.count(),
            'Grades': Grade.objects.count(),
            'Subjects': Subject.objects.count(),
            'Terms': Term.objects.count(),
            'Teachers': Teacher.objects.count(),
            'Parents': Parent.objects.count(),
            'Comments': ReportComment.objects.count(),
            'Classes': Classroom.objects.count(),  # double-check this model exists
        }
        return Response(data)

# Render chart view with data passed into template context
def dashboard_view(request):
    # Make sure Classroom model exists; if not, remove this line or fix the import
    model_data = {
        'Students': Student.objects.count(),
        'Teachers': Teacher.objects.count(),
        'Subjects': Subject.objects.count(),
        'Classes': Classroom.objects.count(),
        'Terms': Term.objects.count(),
        'Parents': Parent.objects.count(),
        'Grades': Grade.objects.count(),
        'Comments': ReportComment.objects.count(),
        'Users': User.objects.count(),
    }

    labels = list(model_data.keys())
    values = list(model_data.values())

    return render(request, 'chart.html', {
        'labels': labels,
        'values': values
    })

def base_view(request):
    context={
        'title': "base page",
    }
    return render(request, 'base.html', context)


def view_student(request):
    students = Student.objects.all()
    context = {
        'title': 'Lists of Students',
        'students': students,
    }
    return render(request, 'student/student.html', context)

def add_student(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student')

    context = {
        'title': 'Add student',
        'form': form
    }
    return render(request, 'student/add_student.html', context)


def update_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('student')
    context ={
        'title': 'Update Student Record',
        'form': form
    }
    return render(request, 'student/add_student.html', context)

def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('student')
    context = {
        'title': 'Student delete page',
        'obj': student
    }
    return render(request, 'delete.html', context)


def view_classroom(request):
    classrooms = Classroom.objects.all()
    context = {
        'title': 'Classes',
        'classrooms': classrooms
    }
    return render(request, 'classroom/classroom.html', context)


def add_classroom(request):
    form = ClassroomForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('classroom')

    context ={
        'title': 'Add classroom',
        'form': form
    }
    return render(request, 'classroom/add_classroom.html', context)

def update_classroom(request, classroom_id):
    classroom = get_object_or_404(Classroom, id=classroom_id)
    form = ClassroomForm(request.POST or None, instance=classroom)
    if form.is_valid():
        form.save()
        return redirect('classroom')
    context = {
        'title': 'Update classroom',
        'form': form
    }
    return render(request, 'classroom/add_classroom.html', context)


def delete_classroom(request, classroom_id):
    classroom = Classroom.objects.get(id=classroom_id)
    if request.method == 'POST':
        classroom.delete()
        return redirect('classroom')
    context = {
        'title' : 'Classroom delete',
        'obj': classroom
    }
    return render(request, 'delete.html', context)


def view_parent(request):
    parents = Parent.objects.all()
    context={
        'title': 'Parents',
        'parents': parents
    }
    return render(request, 'parent/parent.html', context)

def add_parent(request):
    form = ParentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('parent')
    context = {
        'title': 'Add Parent Record',
        'form': form
    }
    return render(request, 'parent/add_parent.html', context)

def update_parent(request, parent_id):
    parent = get_object_or_404(Parent, id=parent_id)
    form = ParentForm(request.POST or None, instance=parent)
    if form.is_valid():
        form.save()
        return redirect('parent')
    context = {
        'title': 'Update Parent',
        'form': form
    }
    return render(request, 'parent/add_parent.html', context)


def delete_parent(request, parent_id):
    parent = Parent.objects.get(id=parent_id)
    if request.method == 'POST':
        parent.delete()
        return redirect('parent')
    context = {
        'title': 'Parent delete',
        'obj': parent
    }
    return render(request, 'delete.html', context)


def view_comment(request):
    comments = ReportComment.objects.all()
    context = {
        'title': 'Comment',
        'comments': comments

    }
    return render(request, 'comment/comment.html', context)

def add_comment(request):
    form = CommentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('comment')
    context = {
        'title': 'Add Comment',
        'form' : form
    }
    return render(request, 'comment/add_comment.html', context)

def update_comment(request, comment_id):
    comment = get_object_or_404(ReportComment, id=comment_id)
    form = CommentForm(request.POST or None, instance=comment)
    if form.is_valid():
        form.save()
        return redirect('comment')
    context = {
        'title': 'Update Comment',
        'form': form
    }
    return render(request, 'comment/add_comment.html', context)

def delete_comment(request, comment_id):
    comment = ReportComment.objects.get(id=comment_id)
    if request.method == 'POST':
        comment.delete()
        return redirect('comment')
    context = {
        'title' : 'Comment delete',
        'obj': comment
    }
    return render(request, 'delete.html', context)

from django.shortcuts import render, redirect, get_object_or_404
from .models import Grade
from .forms import GradeForm

def view_grade(request):
    grades = Grade.objects.all()
    context = {
        'title': 'View Grade',
        'grades': grades
    }
    return render(request, 'grade/grade.html', context)

def add_grade(request):
    form = GradeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('grade')
    context = {
        'title': 'Add grade',
        'form': form
    }
    return render(request, 'grade/add_grade.html', context)

def update_grade(request, grade_id):
    grade = get_object_or_404(Grade, id=grade_id)
    form = GradeForm(request.POST or None, instance=grade)
    if form.is_valid():
        form.save()
        return redirect('grade')
    context = {
        'title': "Update Grade",
        'form': form
    }
    return render(request, 'grade/add_grade.html', context)

def delete_grade(request, grade_id):
    grade = get_object_or_404(Grade, id=grade_id)
    if request.method == 'POST':
        grade.delete()
        return redirect('grade')
    context = {
        'title': 'Grade delete',
        'obj': grade
    }
    return render(request, 'delete.html', context)

def view_teacher(request):
    teachers = Teacher.objects.all()
    context = {
        'title': 'Teachers',
        'teachers': teachers
    }
    return render(request, 'teacher/teacher.html', context)

def add_teacher(request):
    form = TeacherForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('teacher')
    context = {
        'title': 'add teacher',
        'form': form
    }
    return render(request, 'teacher/add_teacher.html', context)


def update_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    form = TeacherForm(request.POST or None, instance=teacher)
    if form.is_valid():
        form.save()
        return redirect('teacher')
    context ={
        'title': 'Teacher update',
        'form': form
    }
    return render(request, 'teacher/add_teacher.html', context)


def delete_teacher(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)
    if request.method =="POST":
        teacher.delete()
        return redirect('teacher')
    context ={
        'title':'delete teacher',
        'obj': teacher
    }
    return render(request, 'delete.html', context)

def view_subject(request):
    subjects = Subject.objects.all()
    context = {
        'title': 'Subject',
        'subjects': subjects
    }
    return render(request, 'subject/subject.html', context)

def add_subject(request):
    form = SubjectForm(request.POST or None)
    if request.method == 'POST':
        form.save()
        return redirect('subject')
    context = {
        'title': 'Add subject',
        'form': form
    }
    return render(request, 'subject/add_subject.html', context)

def update_subject(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    form = SubjectForm(request.POST or None, instance=subject)
    if form.is_valid():
        form.save()
        return redirect('subject')
    context = {
        'title': 'Update subject',
        'form': form
    }
    return render(request, 'subject/add_subject.html', context)

def delete_subject(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    if request.method == 'POST':
        subject.delete()
        return render('subject')
    context = {
        'title': 'Delete subject',
        'obj': subject
    }
    return render(request, 'delete.html', context)

def view_term(request):
    terms = Term.objects.all()
    context = {
        'title': 'Term',
        'terms': terms
    }
    return render(request, 'term/term.html', context)

def add_term(request):
    form = TermForm(request.POST or None)
    if request.method == 'POST':
        form.save()
        return redirect('term')
    context = {
        'title': 'Add term',
        'form': form
    }
    return render(request, 'term/add_term.html', context)
def update_term(request, term_id):
    term = get_object_or_404(Term, id=term_id)
    form = TermForm(request.POST or None, instance=term)
    if request.method =='POST':
        form.save()
        return redirect('term')
    context ={
        'title': 'Update term',
        'form': form
    }
    return render(request, 'term/add_term.html', context)

def delete_term(request, term_id):
    term = Term.objects.get(id=term_id)
    if request.method == 'POST':
        term.delete()
        return redirect('term')
    context ={
        'title': 'Delete term',
        'obj': term
    }
    return render(request, 'delete.html', context)

def subject_avg_scores_chart(request):
    # Select a term (latest or specific)
    term = Term.objects.last()

    # Get average scores per subject for that term
    averages = (
        Grade.objects.filter(term=term)
        .values('subject__name')
        .annotate(avg_score=Avg('score'))
        .order_by('subject__name')
    )

    subjects = [entry['subject__name'] for entry in averages]
    scores = [entry['avg_score'] for entry in averages]

    # Create Bokeh figure
    plot = figure(x_range=subjects, height=400, title=f"Average Scores per Subject ({term.name} {term.year.year})",
                  toolbar_location=None, tools="")
    plot.vbar(x=subjects, top=scores, width=0.5, color="firebrick")

    plot.xgrid.grid_line_color = None
    plot.y_range.start = 0
    plot.y_range.end = 100
    plot.xaxis.major_label_orientation = 1

    # Extract components
    script, div = components(plot)

    return render(request, 'charts/subject_scores.html', {
        'bokeh_script': script,
        'bokeh_div': div,
        'term': term
    })
