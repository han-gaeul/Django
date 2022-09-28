from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.

def index(request):
    todos = Todo.objects.all().order_by('id')
    context = {
        'todos' : todos,
    }
    return render(request, 'todos/index.html', context)

def create(request):
    content = request.GET.get('content')
    priority = request.GET.get('priority')
    created_at = request.GET.get('created_at')
    deadline = request.GET.get('deadline')
    Todo.objects.create(content=content, priority=priority, deadline=deadline, created_at=created_at)

    return redirect('todos:index')

def delete(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk).delete()
    return redirect('todos:index')

def completed(request, todo_pk):
    update = Todo.objects.get(pk=todo_pk)
    update.completed = True
    update.save()
    return redirect('todos:index')