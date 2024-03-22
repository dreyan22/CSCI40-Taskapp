from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello World! This came from the index view.')

def task_list(request):
    ctx = {
        "tasks": [
            "task 1",
            "task 2",
            "task 3",
            "task 4"
        ]
    }
    return render(request, "tasks/task_list.html", ctx)
