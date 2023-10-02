from django.db import models


class Project(models.Model):
    fio = models.CharField(max_length=255)
    course = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    passport = models.CharField(max_length=20)
    project_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.project_name}"
