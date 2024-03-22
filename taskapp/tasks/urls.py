from django.urls import path

from .views import task_list, task_detail, index

urlpatterns = [
    path('', task_list, name="task_list"),
    path('<int:pk>/detail', task_detail, name="task_detail"),
    path('index', index, name='index')
]

app_name = 'tasks'