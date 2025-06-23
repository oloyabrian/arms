import datetime
from datetime import timezone
from django.utils import timezone


from django.db import models
from django.db.models import CASCADE


# Create your models here.


class Term(models.Model):
    name = models.CharField(max_length=50)
    year = models.DateField(default=datetime.date.today())


    def __str__(self):
        return f"{self.name} {self.year}"

class Parent(models.Model):
    SEX_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    sex = models.CharField(max_length=6, choices=SEX_CHOICES, default='Male')  # Fixed
    address = models.CharField(max_length=100)
    tel = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"


class Teacher(models.Model):
    SEX_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    sex = models.CharField(max_length=6, choices=SEX_CHOICES, default='Male')
    date_employed = models.DateField(default=datetime.date.today())
    address = models.CharField(max_length=50)
    tel = models.CharField(max_length=30)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"


class Classroom(models.Model):
    name = models.CharField(max_length=50)
    capacity = models.CharField(max_length=3)
    current_population = models.CharField(max_length=3)
    class_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f" {self.name} "

class Student(models.Model):
    SEX_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    student_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    sex = models.CharField(max_length=6, choices=SEX_CHOICES, default='Male')
    date_of_birth = models.DateField(default=datetime.date.today())
    date_of_admission = models.DateField(default=timezone.now)
    parent_name = models.ForeignKey(Parent, on_delete=models.CASCADE)
    student_class = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    student_term = models.ForeignKey(Term, on_delete=models.CASCADE)


    def __str__(self):
        return f"MAP {self.student_id}"

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"



class Subject(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.student.name} - {self.subject.name} ({self.term.name}): {self.get_grade_label()}"


    def get_grade_label(self):
        score = float(self.score)
        if 0 <= score <= 29:
            return 'F'
        elif 30 <= score <= 39:
            return 'P8'
        elif 40 <= score <= 44:
            return 'P8'
        elif 45 <= score <= 49:
            return 'P7'
        elif 50 <= score <= 54:
            return 'C6'
        elif 55 <= score <= 59:
            return 'C5'
        elif 60 <= score <= 64:
            return 'C4'
        elif 65 <= score <= 69:
            return 'C3'
        elif 70 <= score <= 79:
            return 'D2'
        elif 80 <= score <= 100:
            return 'D1'
        else:
            return 'Invalid Score'

class ReportComment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    comment = models.TextField()
    date_commented = models.DateField(default=timezone.now)

    def __str__(self):
        return f"Comment for {self.student.name} - {self.term.name}"