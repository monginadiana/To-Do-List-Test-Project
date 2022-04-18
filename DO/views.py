from django.shortcuts import redirect, render, get_object_or_404
 

from DO.models import ToDo
from .forms import TodoForm, updatetodoForm

# Create your views here.

def index(request):
    todo=ToDo.objects.all()
    ctx={ 'todo':todo}
    return render(request, 'index.html', ctx)

def create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST, request.FILES)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
        return redirect('/')
    else:
            form = TodoForm()
    
    return render(request, 'form.html', {'form':form})

def singleToDo(request, todo_id):
    todo=ToDo.objects.filter(id=todo_id)
    ctx={ 'todo':todo}
    return render(request, 'singleToDo.html', ctx)

def update_todo(request, todo_id):
    updateTodo = ToDo.objects.get(id=todo_id)
    form = updatetodoForm(instance=updateTodo)
    if request.method == "POST":
            form = updatetodoForm(request.POST,request.FILES,instance=updateTodo)
            if form.is_valid():  
                
                updateTodo = form.save(commit=False)
                updateTodo.save()
                return redirect('/') 
            
    ctx = {"form":form}
    return render(request, 'update_todo.html' , ctx)

def delete_todo(request, todo_id):
    obj = get_object_or_404(ToDo, id=todo_id)
    if request.method == "POST":
        obj.delete()
        return redirect('/') 
            
    ctx = {}
    return render(request, 'delete_todo.html', ctx)