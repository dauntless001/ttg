import random
from course.models import Course
from department.models import Department
from room.models import Room
from timetable.utils.func import get_level_course
from timetable.utils.choices import Level
'''
Conditions
Maximum Course for each level in a semester = 14
Other free slots can serve as practical classes or free periods
'''

def gen_timetable(department, semester):
    days = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri']
    timetable = [] 
    venues = [a for a in Room.objects.filter(department__id=department).values_list('name', 'capacity')]
    courses = {
        'nd1_courses' : get_level_course(department, Level.NDI, semester),
        'nd2_courses' : get_level_course(department, Level.NDII, semester),
        'hnd1_courses' : get_level_course(department, Level.HNDI, semester),
        'hnd2_courses' : get_level_course(department, Level.HNDII, semester)

    }
    levels = ['nd1', 'nd2', 'hnd1', 'hnd2']
    if len(venues) > -1:
        for day in days:
            # initial day list
            dayList = []
            day_lecture = {
                day : day,
            }

            for level in levels:
                
                level_course_list = courses[f'{level}_courses'] #Level Specific courses
                course_list = [] # chosen course list
                day_course_list = [] # Level courses selected for each day
                # Maximum of 4 lectures per day except for Wednesday and Friday
                number_of_courses_per_day = 3 if day == 'Wed' or day == 'Fri' else 4
                for a in range(number_of_courses_per_day):
                    course_id = random.randint(0, len(level_course_list)-1)
                    course = level_course_list[course_id]
                    day_course_list.append(course)
                    level_course_list.remove(course)
                # Add Jumat to Wednesday and Friday
                if day == 'Wed' or day == 'Fri':
                    day_course_list.insert(2, ['Jumat', 'Jumat'])
                dayList.append({'level':level, 'lectures' : day_course_list})
                day_course_list = []
            
            
            day_lecture[day] = dayList
            timetable.append(day_lecture)
            dayList = []
    return timetable