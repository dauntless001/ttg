from django.urls import path
from department import views, ajax_views

app_name = 'department'

urlpatterns = [
    path('', views.DepartmentListView.as_view(), name='departments'),
    path('add-department/', ajax_views.add_department, name='add-departments'),
    path('<int:id>/delete/', views.DepartmentDeleteView.as_view(), name='delete-department'),
    path('department/edit/', ajax_views.edit_department, name='edit-department'),
]