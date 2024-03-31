from django.urls import path
from .views import project_list, add_project, edit_project, delete_project

app_name = 'projects'

urlpatterns = [
    path('', project_list, name='project_list'),
    path('add/', add_project, name='add_project'),
    path('<int:project_id>/edit/', edit_project, name='edit_project'),
    path('<int:project_id>/delete/', delete_project, name='delete_project'),
]
