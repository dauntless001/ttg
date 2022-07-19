from course.models import Course

def add_free(number):
    return [[' ', ' '] for a in range(number)]


def get_level_course(department,level,semester):
    courses = [a for a in Course.objects.filter(level=level, semester=semester, department__id=department).values_list('code', 'lecturer', 'venue')]
    return courses+add_free(18-len(courses))