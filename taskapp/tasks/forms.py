from django import forms

from .models import Task, TaskGroup

# Option 1 for 6-TaskUpdate
class TaskForm(forms.ModelForm):
    name = forms.CharField(label='Task Name', max_length=100)
    due_date = forms.DateTimeField(label='Due Date')
    taskgroup = forms.ModelChoiceField(label='Tasl Group',
        queryset=TaskGroup.objects.all()
    )


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'