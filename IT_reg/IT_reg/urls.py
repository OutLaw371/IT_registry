from django.contrib import admin
from django.urls import path
from myapp1.views import home_page, save_project, project_list, project_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='homepage'),
    path('save_project', save_project, name='save_project'),
    path('projects/', project_list, name='project_list'),
    path('/projects/<int:pk>/', project_data, name='project_data'),
]