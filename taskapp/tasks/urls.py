from django.urls import path

from .views import task_list, index

urlpatterns = [
    path('', task_list, name="task_list"),
    path('index', index, name='index')
]

app_name = 'tasks'