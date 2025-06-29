from django.contrib import admin
from core.models import Term, Parent, Teacher, Classroom, Student, Subject, Grade, ReportComment

@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    list_display = ('name', 'year')
    list_filter = ('year',)
    list_editable = ('year',)
    list_per_page = 8
    search_fields = ('name', 'year')
    ordering = ('name' ,)


@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','sex', 'address', 'tel', 'email')
    list_editable = ('address', 'tel', 'email')
    list_filter = ('sex', 'address',)
    list_per_page = 8
    search_fields = ('address', 'email')
    ordering = ('first_name',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'sex', 'date_employed', 'address', 'tel', 'email')
    list_filter = ('sex', 'date_employed', 'address')
    list_editable = ('date_employed', 'address', 'tel', 'email')
    list_per_page = 8
    search_fields = ('address', 'tel', 'email')
    ordering = ('first_name',)



@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity', 'current_population', 'class_teacher')
    list_filter = ('name', 'class_teacher')
    list_editable = ('capacity', 'current_population', 'class_teacher')
    list_per_page = 8
    search_fields = ('name', 'class_teacher__first_name', 'class_teacher__last_name')
    ordering = ('name',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('bug_str', 'first_name', 'last_name', 'sex', 'date_of_birth', 'date_of_admission',
                   'parent_name', 'student_class', 'student_term')
    list_filter = ('student_class', 'student_term')
    list_editable = ('student_class', 'student_term')
    list_per_page = 8
    search_fields = (
        'first_name', 'last_name',
        'parent_name__first_name', 'parent_name__last_name',
        'student_class__name', 'student_term__name'
    )
    ordering = ('first_name',)


    def bug_str(self, obj):
        return str(obj)

    bug_str.short_description = 'Bug'



@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher')
    list_filter = ('name', 'teacher')
    list_editable = ('teacher', )
    list_per_page = 8
    search_fields = ('name', 'teacher__first_name', 'teacher__last_name')
    ordering = ('name',)

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'term', 'get_grade_label_display')
    list_filter = ('student', 'subject', 'term')
    list_editable = ('subject', 'term')
    list_per_page = 8
    search_fields = (
        'student__first_name', 'student__last_name',
        'subject__name', 'term__name',
        'grade_label'
    )
    ordering = ('student',)

    def get_grade_label_display(self, obj):
        return obj.get_grade_label()

    get_grade_label_display.short_description = 'Grade'


@admin.register(ReportComment)
class ReportCommentAdmin(admin.ModelAdmin):
    list_display = ('student', 'term', 'comment')
    list_filter = ('term', 'comment' )
    list_editable = ('term', 'comment')
    list_per_page = 8
    search_fields = (
        'student__first_name', 'student__last_name',
        'term__name', 'comment'
    )
    ordering = ('student',)
