from django.urls import path

from .views import task_list, task_detail, index, TaskListView,TaskDetailView

urlpatterns = [
    # path('list', task_list, name="task_list"), # Option 1 for 5-Tasklist-Input
    # path('<int:pk>/detail', task_detail, name="task_detail"),
    path('', index, name='index'),
    # path('list', TaskListView.as_view(), name="task_list"),
    path('<int:pk>/detail', TaskDetailView.as_view(), name="task_detail")
]

app_name = 'tasks'