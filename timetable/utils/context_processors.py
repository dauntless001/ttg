from course.models import Course
from room.models import Room
from department.models import Department
from home.models import TimeTable

def addOns(request):
    context = {
        'no_of_departments' : Department.objects.all().count(),
        'no_of_courses' : Course.objects.all().count(),
        'no_of_rooms' : Room.objects.all().count(),
        'no_of_timetables' : TimeTable.objects.all().count(),
    }
    return context