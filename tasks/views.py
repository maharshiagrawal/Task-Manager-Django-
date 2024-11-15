from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

from django.shortcuts import get_object_or_404, redirect, render
from .models import Task
from .forms import TaskForm

def task_create(request, task_id=None):
    # Retrieve task if task_id exists, otherwise create a new instance
    task = get_object_or_404(Task, id=task_id) if task_id else None
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()  # Save new or updated task
            return redirect('task_list')  # Redirect to task list after saving
        else:
            print("Form is invalid:", form.errors)  # Print errors for debugging
            
    else:
        # Create a blank form if request is GET or invalid form in POST
        form = TaskForm(instance=task)
        
    # Render the form with context to display in HTML template
    return render(request, 'task_form.html', {'form': form})


def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)  # Fetch the task by primary key
    if request.method == 'POST':  # If the form is submitted
        form = TaskForm(request.POST, instance=task)  # Bind the form to the existing task instance
        if form.is_valid():  # Check if the form is valid
            form.save()  # Save the updated task
            return redirect('task_list')  # Redirect to the task list page
    else:
        form = TaskForm(instance=task)  # If the form is not submitted, display the current task data in the form
    
    return render(request, 'task_form.html', {'form': form})  # Render the form

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'task_confirm_delete.html', {'task': task})
