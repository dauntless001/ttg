from django.urls import path
from home import views

app_name = 'home'

urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('time-tables/', views.TimeTableListView.as_view(), name='timetables'),
    path('time-tables/<int:id>/', views.TimetableDetailView.as_view(), name='timetable-detail'),
    path('time-tables/<int:id>/delete/', views.TimetableDeleteView.as_view(), name='timetable-delete'),
    path('edit-profile/', views.ProfileUpdateView.as_view(), name='edit-profile'),
]