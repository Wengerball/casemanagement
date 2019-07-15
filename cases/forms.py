from django import forms
from cases.models import Cases
from cases.models import Tasks
from django.contrib.auth.models import User


class CaseForm(forms.ModelForm):
    class Meta:
        model = Cases
        exclude = ['casemanager']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        exclude = ['caseid']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
