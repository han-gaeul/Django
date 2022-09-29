from time import timezone
from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.

# 첫번째 read
# 데이터의 목록을 출력
def index(request):
    # DB에서 모든 글을 불러온 다음
    # 목록을 id를 기준으로 정렬해서 출력
    todos = Todo.objects.all().order_by('priority')

    # template에 보냄
    context = {
        'todos' : todos,
    }
    return render(request, 'todos/index.html', context)

def create(request):
    content = request.GET.get('content')
    priority = request.GET.get('priority')
    deadline = request.GET.get('deadline')

    Todo.objects.create(content=content, priority=priority, deadline=deadline)

    return redirect('todos:index')

def delete(request, pk):
    Todo.objects.get(id = pk).delete()
    return redirect('todos:index')

def update(requset, pk):
    todos = Todo.objects.get(id = pk)
    todos.completed = not todos.completed
    todos.save()

    return redirect('todos:index')

def edit(request, pk):
    todos = Todo.objects.get(id = pk)
    context = {
        'todos' : todos
    }

    return redirect('todos:index', context)

def editupdate(request, pk):
    todos = Todo.objects.get(id = pk)
    content = request.POST.get('editContent')
    priority = request.POST.get('editPriority')
    deadline = request.POST.get('editDeadline')
    

    if deadline == '':
        deadline = timezone.now()

    todos.content = content
    todos.priority = priority
    todos.deadline = deadline

    todos.save()

    return redirect('todos:index')