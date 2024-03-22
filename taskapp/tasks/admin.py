from django.contrib import admin

from .models import Task, TaskGroup


class TaskGroupAdmin(admin.ModelAdmin):
    model = TaskGroup


class TaskAdmin(admin.ModelAdmin):
    model = Task


admin.site.register(TaskGroup, TaskGroupAdmin)
admin.site.register(Task, TaskAdmin)