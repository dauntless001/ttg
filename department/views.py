from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import ListView, View
from department.models import Department
# Create your views here.
class DepartmentListView(LoginRequiredMixin, ListView):
    queryset = Department.objects.all()
    template_name = 'department/departments.html'
    context_object_name = 'departments'

class DepartmentDeleteView(LoginRequiredMixin, View):
    def get_department(self):
        return get_object_or_404(Department, id=self.kwargs.get('id'))

    def get(self, request, *args, **kwargs):
        self.get_department().delete()
        messages.success(request, 'Department deleted Successfully')
        return redirect('department:departments')

