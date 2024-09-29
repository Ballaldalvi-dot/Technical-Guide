from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import Todo
from .models import Todo,User
from django.utils import timezone
from django.contrib import messages
from .forms import ShareTaskForm




# Create your views here.
def register(request):
    if request.method == 'GET':
        form = UserCreationForm(request.POST)
        context={"form" : form
                 
        }
        return render(request,'todoapp/register.html',context=context)
    else:
        print(request.POST)
        form = UserCreationForm(request.POST)
        context={"form" : form
                 
        }
        if form.is_valid():
            user=form.save()
            print(user)
            if user is not None:
                return redirect('login')
        else:
            return render(request, 'todoapp/register.html', context=context)

def login_view(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context={"form":form
        }
        return render(request, 'todoapp/login.html', context=context)
    else:
        form=AuthenticationForm(data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                auth_login(request, user)
            return redirect('home')
        else:
            context={"form":form
        }
        return render(request, 'todoapp/login.html', context=context)

def logout_view(request):
    auth_logout(request)
    return redirect('login')



@login_required
def todo_list(request):
    todos = Todo.objects.all()
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'todoapp/todo_list.html', {'todos': todos})


@login_required(login_url='')
def todo_list(request):
    todos= Todo.objects.filter(user=request.user).order_by('reminder')
    if request.user.is_authenticated and not request.user.todos.exists():
        todos = []
    return render(request, 'todoapp/todo_list.html',{'todos':todos})


@login_required(login_url='')
def create_todo(request):
    if request.method=='POST':
        title=request.POST.get('title')
        description=request.POST.get('description')
        reminder=request.POST.get('reminder')
        priority=request.POST.get('priority')
        Todo.objects.create(title=title,description=description,reminder=reminder,priority=priority,user=request.user)

    return redirect('todo_list')

@login_required(login_url='')
def complete_todo(request,todo_id):
    todo= Todo.objects.get(id=todo_id)
    todo.completed=True
    todo.save()
    return redirect('todo_list')

@login_required(login_url='')
def delete_todo(request,todo_id):
    todo= Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('todo_list')

def homepage(request):
    return render(request, 'todoapp/homepage.html')

