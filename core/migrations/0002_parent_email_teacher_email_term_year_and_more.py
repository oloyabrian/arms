# Generated by Django 5.2.2 on 2025-06-08 18:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parent',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='term',
            name='year',
            field=models.DateField(default=datetime.date(2025, 6, 8)),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_admission',
            field=models.DateField(default=datetime.date(2025, 6, 8)),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(default=datetime.date(2025, 6, 8)),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='date_employed',
            field=models.DateField(default=datetime.date(2025, 6, 8)),
        ),
    ]
