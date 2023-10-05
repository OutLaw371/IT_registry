from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from myapp1.views import home_page, save_project, project_list, project_data, delete_project, edit_project
from registration.views import register, profile, login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='homepage'),
    path('save_project', save_project, name='save_project'),
    path('projects/', project_list, name='project_list'),
    path('projects/<int:pk>/', project_data, name='project_data'),
    path('projects/<int:project_id>/delete/', delete_project, name='delete_project'),
    path('projects/<int:project_id>/edit/', edit_project, name='edit_project'),
    path('login/register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', login_view, name='login'),
]
