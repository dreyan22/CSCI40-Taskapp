from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Task, TaskGroup

def index(request):
    return HttpResponse('Hello World! This came from the index view.')


# Option 1 for 5-TaskList-Input
def task_list(request):
    tasks = Task.objects.all()
    ctx = {
        'object_list': tasks,
        'taskgroups': TaskGroup.objects.all()
    }
    if request.method == 'POST':
        task = Task()
        task.name = request.POST.get('task_name')
        task.due_date = request.POST.get('task_due')
        task.taskgroup = TaskGroup.objects.get(pk=request.POST.get('taskgroup'))
        task.save()


    return render(request, "task_list.html", ctx)

def task_detail(request, pk):
    task = Task.objects.get(pk=pk)
    ctx = {
        'task': task
    }
    return render(request, "task_detail.html", ctx)


# # Option 2 for 5-Tasklist-Input
class TaskListView(ListView):
    model = Task
    template_name = "task_list.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["taskgroups"] = TaskGroup.objects.all()
        return ctx
    
    def post(self, request, *args, **kwargs):
        task = Task()
        task.name = request.POST["task_name"]
        task.due_date = request.POST["task_due"]
        task.taskgroup = TaskGroup.objects.get(pk=request.POST.get("taskgroup"))
        task.save()

        return self.get(request, *args, **kwargs)


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "task_detail.html"