from django import forms
from django.forms import TextInput

from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'student_id': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'first_name': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'last_name': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'sex': forms.Select(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'date_of_admission': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter your comment here...'
            }),
            'parent_name':forms.Select(attrs={'class': 'form-control'}),
            'student_class': forms.Select(attrs={'class': 'form-control'}),
            'student_term': forms.Select(attrs={'class': 'form-control'}),

        }


class ClassroomForm(forms.ModelForm):
    class Meta:
        model = Classroom
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'capacity': forms.TextInput(attrs={'class': 'form-control'}),
            'current_population': forms.TextInput(attrs={'class': 'form-control'}),
            'class_teacher': forms.Select(attrs={'class': 'form-select'}),
        }

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'sex': forms.Select(attrs={'class': 'form-control'}),  # assuming choices
            'date_employed': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'tel': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class TermForm(forms.ModelForm):
    class Meta:
        model = Term
        fields = '__all__'
        widgets ={
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
        }

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'
        widgets ={
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'teacher': forms.Select(attrs={'class': 'form-control'})
        }

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = '__all__'
        widgets ={
            'student': forms.Select(attrs={'class': 'form-control'}),
            'subject': forms.Select(attrs={'class': 'form-control', 'rows': 3}),
            'term': forms.Select(attrs={'class': 'form-control', 'rows': 3}),
            'score': forms.TextInput(attrs={'class': 'form-control'}),

        }

from django import forms
from .models import ReportComment

class CommentForm(forms.ModelForm):
    class Meta:
        model = ReportComment
        fields = '__all__'
        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),
            'term': forms.Select(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter your comment here...'
            }),
            'date_commented': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }

class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'sex': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'tel': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }
