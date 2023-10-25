from django.shortcuts import render, redirect
from .models import add_task, todo
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
import random

# Create your views here.
def start(request):
    new = todo()
    new.id = random.randint(1, 10000)
    id = new.id
    return render(request, 'index.html', {'id':id})

def new_to_do (request):
    all_tasks = add_task.objects.all()
    return render(request, 'to-do.html', {'all_tasks': all_tasks})

def new_task(request):
    p = request.POST['task']
    t = add_task()
    t.name = p
    t.id = random.randint(1, 1000)
    t.done = False
    t.save()
    all_tasks = add_task.objects.all()
    return render(request, 'to-do.html', {'all_tasks': all_tasks})


def make_done(request):
    tasks = add_task.objects.all()
    task_id = request.POST['task_id']
    task = add_task.objects.get(id=task_id)
    if task.done == True:
        task.done = False
    else:
        task.done = True
    task.save()
    return render(request, 'to-do.html', {'all_tasks': tasks})

def delete_task(request):
    tasks = add_task.objects.all()
    task_id = request.POST['task_id']
    task = add_task.objects.get(id=task_id)
    if task:
        task.delete()
    return render(request, 'to-do.html', {'all_tasks': tasks})
