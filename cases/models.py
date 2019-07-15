from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class Cases(models.Model):
    caseid = models.IntegerField(unique=True)
    casename = models.CharField(max_length=20)
    casedate = models.DateField()
    casedesc = models.TextField(max_length=200)
    casemanager = models.CharField(max_length=15)

    class Meta:
        db_table = "cases"


class Tasks(models.Model):
    caseid = models.IntegerField()
    taskname = models.CharField(max_length=20, unique=True)
    taskdate = models.DateField()
    taskdesc = models.TextField(max_length=200)
    taskmanager = models.CharField(max_length=15)

    class Meta:
        db_table = "tasks"


class User(AbstractBaseUser):
    username = models.CharField(max_length=20, unique=True)

    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)  # a superuser
