from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from django.shortcuts import redirect

# Create your views here.
def todo_list(request):
    todos = Todo.objects.all()
    return render(request,'todo/index.html',{'todos':todos})

def create_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        created_at = request.POST.get('created_at') 
        due_date = request.POST.get('due_date')
        priority = request.POST.get('priority')

        if title:  # Ensure that title is provided
            Todo.objects.create(title=title, description=description, created_at=created_at, due_date=due_date, priority=priority)
        else:
            return render(request, 'todo/create.html', {'error': 'Title is required.'})

    return redirect('todo_list')


def complete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.completed = not todo.completed  
    todo.save()
    return redirect('todo_list')

def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    if request.method == 'POST':
        todo.delete()  # Delete the task
        return redirect('todo_list')
    return render(request, 'todo/delete_confirm.html', {'todo': todo})