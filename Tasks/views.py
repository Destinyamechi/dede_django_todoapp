from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *


# tasklist view
def index(request):
    tasks = Task.objects.all()
    context = {'tasks':tasks}
    return render(request, 'tasklist.html', context)


# taskform view
def taskForm(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = TaskForm()   
    context = {'tasks':tasks,'form':form}
    return render(request, 'taskform.html', context)


# updatetask view
def updateTask(request, pk):
    tasks = Task.objects.get(id=pk)
    form = TaskForm(instance=tasks)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'updatetask.html', context)


# deletetask view
def deleteTask(request, pk):
    item = Task.objects.get(id=pk)
        
    if request.method == "POST":
        item.delete()
        return redirect('/')
    
    context = {'item':item}
    return render(request,'taskdelete.html', context)
    
