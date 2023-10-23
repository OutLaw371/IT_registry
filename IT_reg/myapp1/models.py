from django.contrib.auth.models import User
from django.db import models


class Project(models.Model):
    fio = models.CharField(max_length=255)
    course = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    passport = models.CharField(max_length=20)
    project_name = models.CharField(max_length=255)
    annotations = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.project_name}"

    class Meta:
        permissions = [
            ('modify_project', 'Can change the project'),
        ]
