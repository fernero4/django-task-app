from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .forms import TaskForm
from .models import Task
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required


# Create your views here.


def Home(request):
    return render(request, 'home.html')


def SingUp(request):

    if request.method == 'GET':
        return render(request, 'sing_up.html', {
            'form': UserCreationForm
        })

    if request.POST['password1'] == request.POST['password2']:
        try:
            user = User.objects.create_user(
                username=request.POST['username'], password=request.POST['password1'])
            user.save()
            login(request, user)
            return redirect('tasks')

        except:
            return render(request, 'sing_up.html', {
                'form': UserCreationForm,
                'error': 'User already exists'
            })
    else:
        return render(request, 'sing_up.html', {
            'form': UserCreationForm,
            'error': 'Password did not match'
        })


@login_required
def SingOut(request):
    logout(request)
    return redirect('Home')


def SingIn(request):

    if request.method == 'GET':
        return render(request, 'sing_in.html', {
            'form': AuthenticationForm,
        })

    if request.method == 'POST':
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'sing_in.html', {
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('Task')


@login_required
def Tasks_Completed(request):
    tasks = Task.objects.filter(
        user=request.user, datecompleted__isnull=False).order_by('-datecompleted')

    return render(request, 'task.html', {'tasks': tasks})


@login_required
def GetTask(request):
    try:
        tasks = Task.objects.filter(
            user=request.user, datecompleted__isnull=True).order_by('-datecompleted')
        return render(request, 'task.html', {'tasks': tasks})
    except:
        return render(request, 'task.html', {'error': 'there is a problem'})


@login_required
def CreateTask(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {
            'form': TaskForm,
        })
    if request.method == 'POST':
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except:
            return render(request, 'create_task.html', {
                'form': TaskForm,
                'Error': 'Incorrect data'
            })


@login_required
def TaskDetail(request, task_id):
    try:
        if request.method == 'GET':
            task = get_object_or_404(Task, pk=task_id, user=request.user)
            form = TaskForm(instance=task)
            return render(request, 'task_detail.html', {'task': task, 'form': form})
        else:
            task = get_object_or_404(Task, pk=task_id, user=request.user)
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('Task')
    except:
        return render(request, 'task_detail.html', {'task': task, 'form': form, 'error': 'there is a problem updating the task'})


@login_required
def CompleteTask(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        return redirect('Task')


@login_required
def DeleteTask(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('Task')
