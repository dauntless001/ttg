from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from department.models import Department

def add_department(request):
    name = request.POST.get('value')
    department, _ = Department.objects.get_or_create(name=name)
    message = f'Department {name} created successfully'
    if not _:
        print(_)
        message = f'Department with name : {name} already exist'
    data = {
        'message' : message,
        'created' : _,
    }
    return JsonResponse(data)

def edit_department(request):
    department = get_object_or_404(Department, id=request.POST.get('id'))
    department.name = request.POST.get('value')
    department.save()
    message = f'Department updated successfully'
    data = {
        'message' : message,
    }
    return JsonResponse(data)