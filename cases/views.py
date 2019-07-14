from django.shortcuts import render, redirect
from cases.forms import CaseForm
from cases.forms import TaskForm
from cases.forms import UserForm
from cases.models import Cases
from cases.models import Tasks
from django.contrib.auth import authenticate, login

# Create your views here.


def redirection(request):
    user = request.user
    if user.is_authenticated==False:
        return redirect('/login.html')
    return redirect("/view.html")


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password,request=request)
        if user is not None:
            login(request, user)
            return redirect('/view.html')
        else:
            return redirect('/login.html')

    form = UserForm()
    return render(request, 'login.html', {'form': form})


def dashboard(request):
    case = Cases.objects.filter(casemanager=request.user.username)
    return render(request, 'view.html', {'cases': case})


def addcase(request):
    if request.method == "POST":
        form = CaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')
    else:
        form = CaseForm()
    return render(request, 'addcase.html', {'form': form})


def addtask(request, id1):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            p = form.save(commit=False)
            p.caseid = id1
            p.save()
            return redirect('/viewtask')
    else:
        form = TaskForm()
    return render(request, 'addtask.html', {'form': form})


def viewtask(request, id1):
    tasks = Tasks.objects.filter(caseid=id1)
    return render(request, 'viewtask.html', {'tasks': tasks})


def editcase(request, id1):
    case = Cases.objects.filter(caseid=id1)
    if request.method == "POST":
        form = CaseForm(request.POST, instance=case)
        if form.is_valid():
            form.save()
            return redirect('/view')
    
    form = CaseForm(instance=case)
    return render(request, 'editcase.html', {'form': form})


def edittask(request, id1):
    task = Tasks.objects.filter(pk=id1)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/viewtask')  
    
    form = CaseForm(instance=case)
    return render(request, 'edittask.html', {'form': form})    


def case(request):
    if request.method == "POST":
        form = CaseForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/view.html')
            except:
                pass
    else:
        form = CaseForm()
    return render(request, 'addcase.html', {'form': form})


def task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/viewtask')
            except:
                pass
    else:
        form = TaskForm()
    return render(request, 'addtask.html', {'form': form})


def showcase(request):
    case1 = Cases.objects.all()
    return render(request, "view.html", {'cases': case1})


def showtask(request):
    task1 = Tasks.objects.all()
    return render(request, "viewtask.html", {'tasks': task1})


def deletecase(request, id1):
    querycase = Cases.objects.get(caseid=id1)
    querycase.delete()
    return render(request, "view.html", {'cases': querycase})


def deletetask(request, name):
    querytask = Tasks.objects.get(taskname=name)
    querytask.delete()
    return render(request, "viewtask.html", {'cases': querytask})
