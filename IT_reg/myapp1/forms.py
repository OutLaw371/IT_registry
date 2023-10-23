from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['fio', 'course', 'email', 'phone', 'passport', 'project_name', 'annotations']
        # labels = {'fio': 'Фамилия',
        #           'course': 'курс',
        #           'email': 'почта',
        #           'phone': 'Телефон',
        #           'passport': 'Паспорт',
        #           'project_name': 'Название проекта',
        #           'annotations': 'Аннотация'}
