from django.contrib import admin

from .models import Task, TaskGroup


class TaskInline(admin.TabularInline):
    model = Task


class TaskGroupAdmin(admin.ModelAdmin):
    inlines = [TaskInline,]


class TaskAdmin(admin.ModelAdmin):
    model = Task

    search_fields = ('name',)

    list_display = ('name', 'due_date',)

    list_filter = ('due_date', )

    fieldsets = [
        ('Details', {
            'fields': [
                ('name', 'due_date'), 'taskgroup'
            ]
        }
        ),
    ]


admin.site.register(TaskGroup, TaskGroupAdmin)
admin.site.register(Task, TaskAdmin)