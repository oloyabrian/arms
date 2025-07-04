# Generated by Django 5.2.2 on 2025-06-08 16:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('capacity', models.CharField(max_length=3)),
                ('current_population', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('tel', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_employed', models.DateField()),
                ('address', models.CharField(max_length=50)),
                ('tel', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=20, unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('date_of_admission', models.DateField()),
                ('parent_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.parent')),
                ('student_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.classroom')),
                ('student_term', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.term')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.teacher')),
            ],
        ),
        migrations.AddField(
            model_name='classroom',
            name='class_teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.teacher'),
        ),
        migrations.CreateModel(
            name='ReportComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.student')),
                ('term', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.term')),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.DecimalField(decimal_places=2, max_digits=5)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.subject')),
                ('term', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.term')),
            ],
        ),
    ]
