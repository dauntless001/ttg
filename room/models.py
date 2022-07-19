import auto_prefetch
from django.db import models
from timetable.utils.choices import VenueType
from timetable.utils.models import NamedTimeBasedModel
# Create your models here.
class Room(NamedTimeBasedModel):
    capacity = models.PositiveIntegerField()
    department = auto_prefetch.ForeignKey('department.Department', on_delete=models.CASCADE)
    type = models.CharField(max_length=30, choices=VenueType.choices, 
        default=VenueType.classroom)
    
    def __str__(self):
        return f'{self.name}'