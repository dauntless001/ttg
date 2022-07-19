from django import forms
from course.models import Course

from timetable.utils.forms import CssForm


class CourseForm(forms.ModelForm,CssForm):
    class Meta:
        model = Course
        exclude = ['visible']