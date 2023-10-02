from django.shortcuts import render, redirect, get_object_or_404
from .forms import Project


def home_page(request):
    return render(request, 'homepage.html')


def save_project(request):
    fio = request.POST.get('fio')
    course = request.POST.get('course')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    passport = request.POST.get('passport')
    project_name = request.POST.get('project_name')

    if (request.method == 'POST' and all([fio, course, email, phone, passport, project_name])):

        project = Project(fio=fio, course=course, email=email, phone=phone, passport=passport,
                          project_name=project_name)
        project.save()

        return render(request, 'success.html')
    else:
        return render(request, 'error.html')


def project_list(request):
    projects = Project.objects.all()
    return render(request, 'BD.html', {'projects': projects})


def project_data(request, pk):
    project = get_object_or_404(Project, pk=pk)
    # projects = Project.objects.all()
    return render(request, 'project_data.html', {'project': project})
