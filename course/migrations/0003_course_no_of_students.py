# Generated by Django 4.0.5 on 2022-07-16 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_course_semester_alter_course_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='no_of_students',
            field=models.PositiveIntegerField(default=0),
        ),
    ]