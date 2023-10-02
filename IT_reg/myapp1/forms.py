from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['fio', 'course', 'email', 'phone', 'passport', 'project_name']
