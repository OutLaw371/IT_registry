from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import Permission
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from .forms import Project, ProjectForm


@login_required
def home_page(request):
    return render(request, 'homepage.html')


def save_project(request):
    fio = request.POST.get('fio')
    course = request.POST.get('course')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    passport = request.POST.get('passport')
    project_name = request.POST.get('project_name')
    annotations = request.POST.get('annotations')

    if (request.method == 'POST' and all([fio, course, email, phone, passport, project_name, annotations])):

        project = Project(fio=fio, course=course, email=email, phone=phone, passport=passport,
                          project_name=project_name, annotations=annotations)
        project.user = request.user
        project.save()

        permission = get_object_or_404(Permission,
                                       codename='modify_project')  # получаем разрешение на изменение проекта
        request.user.user_permissions.add(permission)  # добавляем разрешение текущему пользователю
        return redirect('project_list')
    else:
        return render(request, 'error.html')


@permission_required('myapp1.modify_project')
def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == 'POST':
        project.delete()
        return redirect('/projects/')
    return render(request, 'delete_project.html', {'project': project})


@permission_required('myapp1.modify_project')
# def edit_project(request, project_id):
#     project = get_object_or_404(Project, pk=project_id)
#     if request.method == 'POST':
#         form = ProjectForm(request.POST, instance=project)
#         if form.is_valid():
#             # Сохранение изменений в базе данных
#             form.save()
#
#             # Перенаправление на страницу с деталями проекта
#             return redirect('/projects/' + str(project.id) + '/')
#
#     # Если метод запроса не POST, то создание формы с объектом проекта в качестве экземпляра
#     else:
#         form = ProjectForm(instance=project)
#
#     # Отображение страницы с формой для редактирования
#     return render(request, 'edit_project.html', {'form': form, 'project': project})
def edit_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id) # получаем объект проекта по id
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project) # создаем форму с данными проекта
        if form.is_valid():
            # Сохранение изменений в базе данных
            form.save()

            # Перенаправление на страницу с деталями проекта
            return redirect('/projects/' + str(project.id) + '/')

    # Если метод запроса не POST, то создание формы с объектом проекта в качестве экземпляра
    else:
        form = ProjectForm(instance=project) # создаем форму с данными проекта

    # Отображение страницы с формой для редактирования
    return render(request, 'edit_project.html', {'form': form, 'project': project})


@login_required
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'BD.html', {'projects': projects})


@login_required
def project_data(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_data.html', {'project': project})
