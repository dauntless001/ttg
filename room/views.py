from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import ListView, View
from room.forms import RoomForm
from room.models import Room
# Create your views here.
class RoomListView(LoginRequiredMixin, ListView):
    queryset = Room.objects.all()
    template_name = 'room/rooms.html'
    context_object_name = 'rooms'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['form'] = RoomForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Room Created Successfully')
        return redirect('room:rooms')


class RoomDeleteView(LoginRequiredMixin, View):
    def get_room(self):
        return get_object_or_404(Room, id=self.kwargs.get('id'))

    def get(self, request, *args, **kwargs):
        self.get_room().delete()
        messages.success(request, 'Room deleted Successfully')
        return redirect('room:rooms')