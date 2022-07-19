from django.urls import path
from room import views

app_name = 'room'

urlpatterns = [
    path('', views.RoomListView.as_view(), name='rooms'),
    path('<int:id>/', views.RoomDeleteView.as_view(), name='room-delete'),
]