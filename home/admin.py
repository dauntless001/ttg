from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from home.models import TimeTable, User

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(TimeTable)