from django.http import HttpResponse
from django.shortcuts import render
from todo_app.models import Task
def home(request):
    # by using order_by you can order the data in which order ypu want to see. Adding - before is used to get the data in decending order
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    completed_tasks = Task.objects.filter(is_completed=True)
    context = {
        'tasks':tasks,
        'completed_tasks':completed_tasks,
    }
    return render(request, 'home.html', context)