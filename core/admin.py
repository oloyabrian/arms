from django.contrib import admin
from core.models import Term, Parent, Teacher, Classroom, Student, Subject, Grade, ReportComment

# Register models with custom admin where needed
@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    list_display = ('name', 'year')
    list_filter = ('name',)

@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','sex', 'address', 'tel', 'email')
    list_filter = ('first_name', 'last_name')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'sex', 'date_employed', 'address', 'tel', 'email')
    list_filter = ('first_name', 'last_name')

@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity', 'current_population', 'class_teacher')
    list_filter = ('name', 'class_teacher')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('bug_str', 'first_name', 'last_name', 'sex', 'date_of_birth', 'date_of_admission',
                   'parent_name', 'student_class', 'student_term')
    list_filter = ('student_class', 'student_term', 'first_name', 'last_name')

    def bug_str(self, obj):
        return str(obj)  # This calls your model's __str__()

    bug_str.short_description = 'Bug'

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher')
    list_filter = ('name', 'teacher')

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'term', 'get_grade_label_display')
    list_filter = ('student', 'subject', 'term')

    def get_grade_label_display(self, obj):
        return obj.get_grade_label()
    get_grade_label_display.short_description = 'Grade'

@admin.register(ReportComment)
class ReportCommentAdmin(admin.ModelAdmin):
    list_display = ('student', 'term', 'comment')
    list_filter = ('student','term', 'comment' )


