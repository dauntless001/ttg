import auto_prefetch
from django.core.exceptions import ValidationError
from django.db import models
from department.models import Department
from timetable.utils.choices import Level, Semester
from timetable.utils.models import NamedTimeBasedModel
# Create your models here.

class Course(NamedTimeBasedModel):
    code = models.CharField(max_length=10, unique=True)
    level = models.CharField(max_length=10, choices=Level.choices, default=Level.NDI)
    semester = models.CharField(max_length=10, choices=Semester.choices, default=Semester.First)
    department = auto_prefetch.ForeignKey('department.Department', on_delete=models.CASCADE)
    # no_of_students = models.PositiveIntegerField(default=0)
    venue = models.CharField(max_length=30, null=True, blank=True)
    lecturer = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name} - {self.code}'
    
    def clean(self, *args, **kwargs):
        courses = Course.objects.filter(department__id=self.department.id, level=self.level)
        number_of_courses = courses.count()
        if number_of_courses > 13:
            raise ValidationError("Maximum Course for Each Level in a Semester is 14")
        super(Course, self).clean(*args, **kwargs)
