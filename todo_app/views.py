from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task
# Create your views here.
def addTask(request):
    task = request.POST['task']   # This is will get the data from the user and post it to the database
    Task.objects.create(task = task) # it will store the data in the database
    return redirect('home') # once we added the task we need to return to the home page by redirecting it will go to the home page.


def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_undone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def edit_task(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('home')
    else:
        context = {
            'get_task':get_task,
        }
        return render(request, 'edit_task.html', context)


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')