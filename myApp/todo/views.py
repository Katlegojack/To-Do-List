from django.shortcuts import render,HttpResponse,redirect

from .models import Task
from .forms import TaskForm

def index(request):

    form = TaskForm()

    tasks = Task.objects.all()

    if request.method =="POST":
        form = TaskForm(request.POST)
        if form.is_valid:
            form.save()
        
        return redirect('/')

    context = {
        'tasks': tasks,
        'TaskForm': form,
    }


    return render(request, 'todo/tasks.html',context)

def updateTask(request,pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)#enables us to see the task the current task we want to update

    if request.method =="POST":
        form = TaskForm(request.POST,instance=task)
        if form.is_valid:
            form.save()
        
            return redirect('/')
    context = {
        'TaskForm': form,
    }


    return render(request, 'todo/update-task.html',context)

def deleteTask(request,pk):
    task = Task.objects.get(id=pk)

    if request.method =="POST":
        task.delete()
        return redirect('/')
    
    context = {
        'task':task
    }

    return render(request,'todo/delete-task.html',context) 