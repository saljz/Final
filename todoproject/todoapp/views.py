from django.shortcuts import render, redirect
from .models import Task
from .forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView


# Create your views here.
def add(request):
    task1 = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = Task(name=name, priority=priority, date=date)
        task.save()
    return render(request, "home.html", {'tsk': task1})


# return render(request, 'details.html',)
# def detail(request):
def delete(request, id):
    if request.method == 'POST':
        task = Task.objects.get(id=id)
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request, id):
    task = Task.objects.get(id=id)
    f = TodoForm(request.POST or None, instance=task)

    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request, 'edit.html', {'f': f, 'task': task})


class TasklistView(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'tsk'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'tsk'

