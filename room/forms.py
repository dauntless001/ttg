from django import forms
from timetable.utils.forms import CssForm
from room.models import Room


class RoomForm(forms.ModelForm,CssForm):
    class Meta:
        model  = Room
        exclude = ['visible']