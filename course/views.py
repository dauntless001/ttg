from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import CreateView,ListView, View
from course.forms import CourseForm
from course.models import Course
# Create your views here.
class CourseListView(LoginRequiredMixin, ListView):
    queryset = Course.objects.all()
    template_name = 'course/courses.html'
    context_object_name = 'courses'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['form'] = CourseForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course Created Successfully')
        return redirect('course:courses')



class CourseDeleteView(LoginRequiredMixin, View):
    def get_department(self):
        return get_object_or_404(Course, id=self.kwargs.get('id'))

    def get(self, request, *args, **kwargs):
        self.get_department().delete()
        messages.success(request, 'Course deleted Successfully')
        return redirect('course:courses')
