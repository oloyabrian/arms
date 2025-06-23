from django.shortcuts import redirect
from django.urls import path
from .import views
from .views import HomeView, get_data, dashboard_view

urlpatterns = [
    path('', lambda request: redirect('dashboard'), name='home'),
    path('dashboard/', dashboard_view, name='dashboard'),

    # path('api/chart/data/', ChartData.as_view()),
    # path('api/data/', ChartData.as_view(), name='api-data'),

    path('', views.base_view, name= "base"),
    # path('chart/subjects/', views.subject_avg_scores_chart, name='subject_avg_scores'),

    path('student/', views.view_student, name= 'student'),
    path('add_student/', views.add_student, name='add_student'),
    path('update_student/<int:student_id>/', views.update_student, name='update_student'),
    path('delete_student/<int:student_id>/', views.delete_student, name='delete_student'),

    path('classroom/', views.view_classroom, name='classroom'),
    path('add_classroom/', views.add_classroom, name='add_classroom'),
    path('update_classroom/<int:classroom_id>/', views.update_classroom, name='update_classroom'),
    path('delete_classroom/<int:classroom_id>/', views.delete_classroom, name='delete_classroom'),

    path('comment/', views.view_comment, name='comment'),
    path('add_comment/', views.add_comment, name='add_comment'),
    path('update_comment/<int:comment_id>/', views.update_comment, name='update_comment'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),

    path('grade/', views.view_grade, name='grade'),
    path('add_grade/', views.add_grade, name='add_grade'),
    path('update_grade/<int:grade_id>/', views.update_grade, name='update_grade'),
    path('delete_grade/<int:grade_id>/', views.delete_grade, name='delete_grade'),

    path('teacher/', views.view_teacher, name='teacher'),
    path('add_teacher/', views.add_teacher, name='add_teacher'),
    path('update_teacher/<int:teacher_id>/', views.update_teacher, name='update_teacher'),
    path('delete_teacher/<int:teacher_id>/', views.delete_teacher, name='delete_teacher'),

    path('subject/', views.view_subject, name='subject'),
    path('add_subject/', views.add_subject, name='add_subject'),
    path('update_subject/<int:subject_id>/', views.update_subject, name='update_subject'),
    path('delete_subject/<int:subject_id>/', views.delete_subject, name='delete_subject'),

    path('term/', views.view_term, name='term',),
    path('add_term/', views.add_term, name='add_term'),
    path('update_term/<int:term_id>/', views.update_term, name='update_term'),
    path('delete_term/<int:term_id>/', views.delete_term, name='delete_term'),

    path('parent/', views.view_parent, name='parent'),
    path('add_parent/', views.add_parent, name='add_parent'),
    path('update_parent/<int:parent_id>/', views.update_parent, name='update_parent'),
    path('delete_parent/<int:parent_id>/', views.delete_parent, name='delete_parent'),

]