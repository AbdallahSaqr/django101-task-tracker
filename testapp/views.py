from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render (request, 'main/base_layout.html')

tasks = [
    {
        'id': 1,
        'title': 'Buy groceries',
        'description': 'Milk, cheese, and bread',
        'done': False
    },    
    {
        'id': 2,
        'title': 'Walk the dog',
        'description': 'Take the dog for a walk in the park',
        'done': False
    },
    {
        'id': 3,
        'title': 'Read a book',
        'description': 'Finish reading "Django for Beginners"',
        'done': False
    },
    {
        'id': 4,
        'title': 'Exercise',
        'description': 'Go for a run or do some yoga',
        'done': False
    }
]

def task_list(request):
    my_context = {
        "tasks": tasks
    }
    return render(request, 'testapp/task_list.html', my_context)

def task_detail(request, *args, **kwargs):
    task_id = kwargs.get('task_id')
    for task in tasks:
        if task.get('id') == int(task_id):
            return render(request, 'testapp/task_detail.html', {"task": task})
        
def _get_task(task_id):
    for task in tasks:
        if task["id"] == int(task_id):
            return task
    return None

def task_delete(request, **kwargs):
    task_id = kwargs.get('task_id')
    task = _get_task(task_id)
    if task:
        tasks.remove(task)
        return redirect('task_list')
    else:
        return HttpResponse('Task not found.', status=404)
    
def get_next_task_id():
    if not tasks:
        return 1
    return max(task['id'] for task in tasks) + 1
def task_create(request):
    if request.method == 'POST':
        new_task = {
            'id': get_next_task_id(),
            'title': request.POST.get('title'),
            'description': request.POST.get('description'),
            'done': False
        }
        tasks.append(new_task)
        return redirect('task_list')
    return render(request, 'testapp/task_create.html')

def task_update(request, task_id):
    task = _get_task(task_id)
    if not task:
        return HttpResponse('Task not found.', status=404)

    if request.method == 'POST':
        task['title'] = request.POST.get('title', task['title'])
        task['description'] = request.POST.get('description', task['description'])
        task['done'] = request.POST.get('done', 'off') == 'on'
        return redirect('task_list')

    return render(request, 'testapp/task_update.html', {'task': task})

