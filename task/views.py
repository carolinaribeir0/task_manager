from django.shortcuts import render, redirect
from .models import Task

def home(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})

def salvar(request):
    description=request.POST.get('description')
    status=request.POST.get('status')
    Task.objects.create(description=description, status=status)
    tasks=Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})

def editar(request, id):
    task = Task.objects.get(id=id)
    return render(request, 'update.html', {'task': task})

def update(request, id):
    description = request.POST.get('description')
    status = request.POST.get('status')
    task = Task.objects.get(id=id)
    task.description = description
    task.status = status
    task.save()
    return redirect(home)

def delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect(home)