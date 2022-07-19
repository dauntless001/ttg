import json
from django.shortcuts import render ,redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, View
from home.forms import ProfileUpdateForm, TimetableForm
from home.models import TimeTable, User
from home.timetable import gen_timetable
from timetable.utils.pdf import render_to_pdf
# Create your views here.

class IndexView(TemplateView):
    template_name = 'home/index.html'

class DashboardView(LoginRequiredMixin,TemplateView):
    template_name = 'home/dashboard.html'

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "home/edit-profile.html"
    model = User
    form_class = ProfileUpdateForm

    def get_object(self):
        return self.request.user

    def get_form(self, **kwargs):
        form = super().get_form(**kwargs)
        return form

    def get_success_url(self):
        messages.success(self.request, "Profile updated successfully")
        return reverse_lazy("home:edit-profile")


class TimeTableListView(LoginRequiredMixin, ListView):
    queryset = TimeTable.objects.all()
    template_name = 'home/timetables.html'
    context_object_name = 'timetables'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['form'] = TimetableForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = TimetableForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            department = form.cleaned_data.get('department')
            semester = form.cleaned_data.get('semester')
            timetable_json = gen_timetable(department.id, semester)
            if not timetable_json:
                messages.success(request, 'Department Must have at least 4 classrooms to generate timetable')
                return redirect('home:timetables')
            timetable = form.save(commit=False)
            timetable.json = json.dumps(timetable_json)
            timetable.save()
            messages.success(request, 'Timetable Created Successfully')
            return redirect('home:timetables')
        context = {
            'form' : form,
            'timetables' : self.queryset
        }
        return render(request, self.template_name, context)


class TimetableDeleteView(LoginRequiredMixin, View):
    def get_timetable(self):
        return get_object_or_404(TimeTable, id=self.kwargs.get('id'))

    def get(self, request, *args, **kwargs):
        self.get_timetable().delete()
        messages.success(request, 'Timetable deleted Successfully')
        return redirect('home:timetables')

class TimetableDetailView(View):
    template_name = 'home/timetable-download.html'
    def get_timetable(self):
        return get_object_or_404(TimeTable, id=self.kwargs.get('id'))
    
    def get(self, request, *args, **kwargs):
        data = json.loads(self.get_timetable().json)
        context = {
            'timetable' : self.get_timetable(),
            'data' : data,
        }
        pdf = render_to_pdf(self.template_name, context)
        return HttpResponse(pdf, content_type='application/pdf')
        # response = HttpResponse(pdf, content_type='application/pdf')
        # response['Content-Disposition'] = f'attachment; filename={self.get_timetable()}.pdf'
        # return response
