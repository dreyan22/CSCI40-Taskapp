from django.shortcuts import render
from django.http import HttpResponse

from .models import Task

def index(request):
    return HttpResponse('Hello World! This came from the index view.')

def task_list(request):
    tasks = Task.objects.all
    ctx = {
        "tasks": tasks
    }
    return render(request, "task_list.html", ctx)
