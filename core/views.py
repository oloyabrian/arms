from django.contrib import messages
from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponseForbidden

from core.models import Student, Grade, Subject, Term, Teacher, Parent, ReportComment

from .forms import *
from .models import *
from django.db.models import Avg

def register_view(request):
    # form = CreateUserForm()
    if request.method =='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('home')
    else:
        form = CreateUserForm()

    context ={
        'form': form,
    }
    return render(request, 'register.html', context)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return  redirect('home')

    else:
        form = AuthenticationForm()
    context ={

    }
    return render(request, 'login.html', context)


def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return redirect('login')


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
@login_required(login_url='login')
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
@login_required(login_url='login')
def base_view(request):
    context={
        'title': "base page",
    }
    return render(request, 'base.html', context)

@login_required(login_url='login')
def view_student(request):
    students = Student.objects.all()
    context = {
        'title': 'Lists of Students',
        'students': students,
    }
    return render(request, 'student/student.html', context)

@login_required(login_url='login')
def add_student(request):
    if not request.user.is_staff and not request.user.is_superuser:
        return HttpResponseForbidden("❌ You are not allowed to add any record.")
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "✅ Student added successfully.")
        return redirect('student')

    context = {
        'title': 'Add student',
        'form': form
    }
    return render(request, 'student/add_student.html', context)

@login_required(login_url='login')
def update_student(request, student_id):
    if not request.user.is_staff and not request.user.is_superuser:
        messages.warning(request, "❌ You are not authorized to perform this action.")
        return redirect(request.META.get('HTTP_REFERER', 'student'))
    student = get_object_or_404(Student, id=student_id)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        messages.success(request, "✅ Student updated successfully.")
        return redirect('student')
    context ={
        'title': 'Update Student Record',
        'form': form
    }
    return render(request, 'student/add_student.html', context)


@login_required(login_url='login')
def delete_student(request, student_id):
    if not request.user.is_staff and not request.user.is_superuser:
        messages.warning(request, "❌ You are not authorized to perform this action.")
        return redirect(request.META.get('HTTP_REFERER') or 'student')  # safe fallback

    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        student.delete()
        messages.success(request, "✅ Student deleted successfully.")
        return redirect('student')

    context = {
        'title': 'Student delete page',
        'obj': student
    }
    return render(request, 'delete.html', context)


@login_required(login_url='login')
def view_classroom(request):
    classrooms = Classroom.objects.all()
    context = {
        'title': 'Classes',
        'classrooms': classrooms
    }
    return render(request, 'classroom/classroom.html', context)


@login_required(login_url='login')
def add_classroom(request):
    if not request.user.is_staff and not request.user.is_superuser:
        messages.warning(request, "❌ You are not authorized to perform this action.")
        return redirect(request.META.get('HTTP_REFERER') or 'classroom')
    form = ClassroomForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "✅ Classroom added successfully.")

        return redirect('classroom')

    context ={
        'title': 'Add classroom',
        'form': form
    }
    return render(request, 'classroom/add_classroom.html', context)

@login_required(login_url='login')
def update_classroom(request, classroom_id):
    if not request.user.is_staff and not request.user.is_superuser:
        messages.warning(request, "❌ You are not authorized to perform this action.")
        return redirect(request.META.get('HTTP_REFERER') or 'classroom')
    classroom = get_object_or_404(Classroom, id=classroom_id)
    form = ClassroomForm(request.POST or None, instance=classroom)
    if form.is_valid():
        form.save()
        messages.success(request, "✅ Classroom updated successfully.")

        return redirect('classroom')
    context = {
        'title': 'Update classroom',
        'form': form
    }
    return render(request, 'classroom/add_classroom.html', context)


@login_required(login_url='login')
def delete_classroom(request, classroom_id):
    if not request.user.is_staff and not request.user.is_superuser:
        messages.warning(request, "❌ You are not authorized to perform this action.")
        return redirect(request.META.get('HTTP_REFERER') or 'classroom')
    classroom = Classroom.objects.get(id=classroom_id)
    if request.method == 'POST':
        classroom.delete()
        messages.success(request, "✅ Classroom deleted successfully.")

        return redirect('classroom')
    context = {
        'title' : 'Classroom delete',
        'obj': classroom
    }
    return render(request, 'delete.html', context)

@login_required(login_url='login')
def view_parent(request):
    parents = Parent.objects.all()
    context={
        'title': 'Parents',
        'parents': parents
    }
    return render(request, 'parent/parent.html', context)

@login_required(login_url='login')
def add_parent(request):
    if not request.user.is_staff and not request.user.is_superuser:
        messages.warning(request, "❌ You are not authorized to perform this action.")
        return redirect(request.META.get('HTTP_REFERER') or 'parent')
    form = ParentForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "✅ Parent added successfully.")

        return redirect('parent')
    context = {
        'title': 'Add Parent Record',
        'form': form
    }
    return render(request, 'parent/add_parent.html', context)


@login_required(login_url='login')
def update_parent(request, parent_id):
    if not request.user.is_staff and not request.user.is_superuser:
        messages.warning(request, "❌ You are not authorized to perform this action.")
        return redirect(request.META.get('HTTP_REFERER') or 'parent')
    parent = get_object_or_404(Parent, id=parent_id)
    form = ParentForm(request.POST or None, instance=parent)
    if form.is_valid():
        form.save()
        messages.success(request, "✅ Parent updated successfully.")
        return redirect('parent')
    context = {
        'title': 'Update Parent',
        'form': form
    }
    return render(request, 'parent/add_parent.html', context)


@login_required(login_url='login')
def delete_parent(request, parent_id):
    if not request.user.is_staff and not request.user.is_superuser:
        messages.warning(request, "❌ You are not authorized to perform this action.")
        return redirect(request.META.get('HTTP_REFERER') or 'parent')
    parent = Parent.objects.get(id=parent_id)
    if request.method == 'POST':
        parent.delete()
        messages.success(request, "✅ Parent deleted successfully.")
        return redirect('parent')
    context = {
        'title': 'Parent delete',
        'obj': parent
    }
    return render(request, 'delete.html', context)


@login_required(login_url='login')
def view_comment(request):
    comments = ReportComment.objects.all()
    context = {
        'title': 'Comment',
        'comments': comments

    }
    return render(request, 'comment/comment.html', context)


@login_required(login_url='login')
def add_comment(request):
    if not request.user.is_staff and not request.user.is_superuser:
        messages.warning(request, "❌ You are not authorized to perform this action.")
        return redirect(request.META.get('HTTP_REFERER') or 'comment')
    form = CommentForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "✅ Comment added successfully.")
        return redirect('comment')
    context = {
        'title': 'Add Comment',
        'form' : form
    }
    return render(request, 'comment/add_comment.html', context)


@login_required(login_url='login')
def update_comment(request, comment_id):
    if not request.user.is_staff and not request.user.is_superuser:
        messages.warning(request, "❌ You are not authorized to perform this action.")
        return redirect(request.META.get('HTTP_REFERER') or 'comment')
    comment = get_object_or_404(ReportComment, id=comment_id)
    form = CommentForm(request.POST or None, instance=comment)
    if form.is_valid():
        form.save()
        messages.success(request, "✅ Comment updated successfully.")
        return redirect('comment')
    context = {
        'title': 'Update Comment',
        'form': form
    }
    return render(request, 'comment/add_comment.html', context)


@login_required(login_url='login')
def delete_comment(request, comment_id):
    if not request.user.is_staff and not request.user.is_superuser:
        messages.warning(request, "❌ You are not authorized to perform this action.")
        return redirect(request.META.get('HTTP_REFERER') or 'comment')
    comment = ReportComment.objects.get(id=comment_id)
    if request.method == 'POST':
        comment.delete()
        messages.success(request, "✅ Comment deleted successfully.")
        return redirect('comment')
    context = {
        'title' : 'Comment delete',
        'obj': comment
    }
    return render(request, 'delete.html', context)

from django.shortcuts import render, redirect, get_object_or_404
from .models import Grade
from .forms import GradeForm

@login_required(login_url='login')
def view_grade(request):
    grades = Grade.objects.all()
    context = {
        'title': 'View Grade',
        'grades': grades
    }
    return render(request, 'grade/grade.html', context)


@login_required(login_url='login')
def add_grade(request):
    if not request.user.is_staff and not request.user.is_superuser:
        messages.warning(request, "❌ You are not authorized to perform this action.")
        return redirect(request.META.get('HTTP_REFERER') or 'grade')
    form = GradeForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "✅ Grade added successfully.")
        return redirect('grade')
    context = {
        'title': 'Add grade',
        'form': form
    }
    return render(request, 'grade/add_grade.html', context)


@login_required(login_url='login')
def update_grade(request, grade_id):
    if not request.user.is_staff and not request.user.is_superuser:
        messages.warning(request, "❌ You are not authorized to perform this action.")
        return redirect(request.META.get('HTTP_REFERER') or 'grade')
    grade = get_object_or_404(Grade, id=grade_id)
    form = GradeForm(request.POST or None, instance=grade)
    if form.is_valid():
        form.save()
        messages.success(request, "✅ Grade updated successfully.")
        return redirect('grade')
    context = {
        'title': "Update Grade",
        'form': form
    }
    return render(request, 'grade/add_grade.html', context)


@login_required(login_url='login')
def delete_grade(request, grade_id):
    if not request.user.is_staff and not request.user.is_superuser:
        messages.warning(request, "❌ You are not authorized to perform this action.")
        return redirect(request.META.get('HTTP_REFERER') or 'grade')
    grade = get_object_or_404(Grade, id=grade_id)
    if request.method == 'POST':
        grade.delete()
        messages.success(request, "✅ Grade deleted successfully.")
        return redirect('grade')
    context = {
        'title': 'Grade delete',
        'obj': grade
    }
    return render(request, 'delete.html', context)

@login_required(login_url='login')
def view_teacher(request):
    teachers = Teacher.objects.all()
    context = {
        'title': 'Teachers',
        'teachers': teachers
    }
    return render(request, 'teacher/teacher.html', context)


@login_required(login_url='login')
def add_teacher(request):
    if not request.user.is_staff and not request.user.is_superuser:
        messages.warning(request, "❌ You are not authorized to perform this action.")
        return redirect(request.META.get('HTTP_REFERER') or 'teacher')
    form = TeacherForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "✅ Teacher added successfully.")
        return redirect('teacher')
    context = {
        'title': 'add teacher',
        'form': form
    }
    return render(request, 'teacher/add_teacher.html', context)

@login_required(login_url='login')
def update_teacher(request, teacher_id):
    if not request.user.is_staff and not request.user.is_superuser:
        messages.warning(request, "❌ You are not authorized to perform this action.")
        return redirect(request.META.get('HTTP_REFERER') or 'teacher')
    teacher = get_object_or_404(Teacher, id=teacher_id)
    form = TeacherForm(request.POST or None, instance=teacher)
    if form.is_valid():
        form.save()
        messages.success(request, "✅ Teacher updated successfully.")
        return redirect('teacher')
    context ={
        'title': 'Teacher update',
        'form': form
    }
    return render(request, 'teacher/add_teacher.html', context)

@login_required(login_url='login')
def delete_teacher(request, teacher_id):
    if not request.user.is_staff and not request.user.is_superuser:
        messages.warning(request, "❌ You are not authorized to perform this action.")
        return redirect(request.META.get('HTTP_REFERER') or 'teacher')
    teacher = Teacher.objects.get(id=teacher_id)
    if request.method =="POST":
        teacher.delete()
        messages.success(request, "✅ Teacher deleted successfully.")
        return redirect('teacher')
    context ={
        'title':'delete teacher',
        'obj': teacher
    }
    return render(request, 'delete.html', context)

@login_required(login_url='login')
def view_subject(request):
    subjects = Subject.objects.all()
    context = {
        'title': 'Subject',
        'subjects': subjects
    }
    return render(request, 'subject/subject.html', context)


@login_required(login_url='login')
def add_subject(request):
    if not request.user.is_staff and not request.user.is_superuser:
        messages.warning(request, "❌ You are not authorized to perform this action.")
        return redirect(request.META.get('HTTP_REFERER') or 'subject')
    form = SubjectForm(request.POST or None)
    if request.method == 'POST':
        form.save()
        messages.success(request, "✅ Subject added successfully.")
        return redirect('subject')
    context = {
        'title': 'Add subject',
        'form': form
    }
    return render(request, 'subject/add_subject.html', context)


@login_required(login_url='login')
def update_subject(request, subject_id):
    if not request.user.is_staff and not request.user.is_superuser:
        messages.warning(request, "❌ You are not authorized to perform this action.")
        return redirect(request.META.get('HTTP_REFERER') or 'subject')
    subject = get_object_or_404(Subject, id=subject_id)
    form = SubjectForm(request.POST or None, instance=subject)
    if form.is_valid():
        form.save()
        messages.success(request, "✅ Subject updated successfully.")
        return redirect('subject')
    context = {
        'title': 'Update subject',
        'form': form
    }
    return render(request, 'subject/add_subject.html', context)

@login_required(login_url='login')
def delete_subject(request, subject_id):
    if not request.user.is_staff and not request.user.is_superuser:
        messages.warning(request, "❌ You are not authorized to perform this action.")
        return redirect(request.META.get('HTTP_REFERER') or 'subject')
    subject = Subject.objects.get(id=subject_id)
    if request.method == 'POST':
        subject.delete()
        messages.success(request, "✅ Subject deleted successfully.")
        return render('subject')
    context = {
        'title': 'Delete subject',
        'obj': subject
    }
    return render(request, 'delete.html', context)


@login_required(login_url='login')
def view_term(request):
    terms = Term.objects.all()
    context = {
        'title': 'Term',
        'terms': terms
    }
    return render(request, 'term/term.html', context)


@login_required(login_url='login')
def add_term(request):
    if not request.user.is_staff and not request.user.is_superuser:
        messages.warning(request, "❌ You are not authorized to perform this action.")
        return redirect(request.META.get('HTTP_REFERER') or 'term')
    form = TermForm(request.POST or None)
    if request.method == 'POST':
        form.save()
        messages.success(request, "✅ Term added successfully.")
        return redirect('term')
    context = {
        'title': 'Add term',
        'form': form
    }
    return render(request, 'term/add_term.html', context)

@login_required(login_url='login')
def update_term(request, term_id):
    if not request.user.is_staff and not request.user.is_superuser:
        messages.warning(request, "❌ You are not authorized to perform this action.")
        return redirect(request.META.get('HTTP_REFERER') or 'term')
    term = get_object_or_404(Term, id=term_id)
    form = TermForm(request.POST or None, instance=term)
    if request.method =='POST':
        form.save()
        messages.success(request, "✅ Term updated successfully.")
        return redirect('term')
    context ={
        'title': 'Update term',
        'form': form
    }
    return render(request, 'term/add_term.html', context)


@login_required(login_url='login')
def delete_term(request, term_id):
    if not request.user.is_staff and not request.user.is_superuser:
        messages.warning(request, "❌ You are not authorized to perform this action.")
        return redirect(request.META.get('HTTP_REFERER') or 'term')
    term = Term.objects.get(id=term_id)
    if request.method == 'POST':
        term.delete()
        messages.success(request, "✅ Term deleted successfully.")
        return redirect('term')
    context ={
        'title': 'Delete term',
        'obj': term
    }
    return render(request, 'delete.html', context)


@login_required(login_url='login')
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
