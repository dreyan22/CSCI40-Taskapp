from django.urls import path

from .views import task_list, task_detail, index, TaskListView,TaskDetailView

urlpatterns = [
    # path('', task_list, name="task_list"),
    path('', TaskListView.as_view(), name="task_list"),
    # path('<int:pk>/detail', task_detail, name="task_detail"),
    path('<int:pk>/detail', TaskDetailView.as_view(), name="task_detail"),
    path('index', index, name='index')
]

app_name = 'tasks'