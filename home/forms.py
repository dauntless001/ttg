from django import forms
from home.models import TimeTable, User
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm
from timetable.utils.forms import CssForm


class ProfileUpdateForm(UserChangeForm, CssForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "username"
        ]

        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "First name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Last name"}),
            "email": forms.EmailInput(
                attrs={"placeholder": "Email address", "readonly": True}
            ),
            "username": forms.TextInput(
                attrs={"placeholder": "Username",}
            ),
        }


class PasswordUpdateForm(PasswordChangeForm, CssForm):
    class Meta:
        model = User
        fields = "__all__"

class TimetableForm(forms.ModelForm,CssForm):
    class Meta:
        model = TimeTable
        exclude = ['visible', 'json']