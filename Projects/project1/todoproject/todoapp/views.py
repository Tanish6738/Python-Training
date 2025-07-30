from django.shortcuts import render, redirect, get_object_or_404
from todoapp.models import Todo

def task_list(request):
    tasks = Todo.objects.all().order_by('-created_at')
    return render(request, 'todoapp/task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST.get('description', '')
        Todo.objects.create(title=title, description=description)
        return redirect('task_list')
    return render(request, 'todoapp/task_form.html')

def task_update(request, task_id):
    task = get_object_or_404(Todo, id=task_id)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST.get('description', '')
        task.save()
        return redirect('task_list')
    return render(request, 'todoapp/task_form.html', {'task': task})

def task_delete(request, task_id):
    task = get_object_or_404(Todo, id=task_id)
    task.delete()
    return redirect('task_list')

def task_toggle(request, task_id):
    task = get_object_or_404(Todo, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')
