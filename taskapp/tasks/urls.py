from django.urls import path

from .views import task_list, task_detail, index, TaskListView,TaskDetailView, TaskCreateView, TaskUpdateView

urlpatterns = [
    # path('list', task_list, name="task_list"), # Option 1 for 5-Tasklist-Input and 6-TaskUpdate
    # path('<int:pk>/detail', task_detail, name="task_detail"),
    path('', index, name='index'),
    path('create', TaskCreateView.as_view(), name='create'),
    path('list', TaskListView.as_view(), name="task_list"), # Option 2 for 5-Tasklist-Input and 6-TaskUpdate
    path('<int:pk>/detail', TaskUpdateView.as_view(), name="task_detail"),
    # path('<int:pk>/detail', TaskDetailView.as_view(), name="task_detail")
]

app_name = 'tasks'