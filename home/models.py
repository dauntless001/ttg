import auto_prefetch
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import ValidationError
from timetable.utils.choices import Level, Semester
from timetable.utils.models import TimeBasedModel
import jsonfield
# Create your models here.

class User(AbstractUser):
    def __str__(self):
        return self.get_full_name() or self.email


class TimeTable(TimeBasedModel):
    department = auto_prefetch.ForeignKey('department.Department', on_delete=models.CASCADE)
    semester = models.CharField(max_length=20, choices=Semester.choices, default=Semester.First)
    json = jsonfield.JSONField()

    def __str__(self):
        # return f'Timetable for {self.department}- {self.semester} Semester'
        return f'Provisional Timetable for {self.semester} Semester'.upper()
    
    def clean(self, *args, **kwargs):
        timetables = TimeTable.objects.filter(department__id=self.department.id, semester=self.semester)
        number_of_occurence = timetables.count()
        if number_of_occurence > 0:
            raise ValidationError("Each Department can only have 1 timetable at a time. Delete existing one and generate a new one")
        super(TimeTable, self).clean(*args, **kwargs)