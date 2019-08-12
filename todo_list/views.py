from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import TODO
from .forms import TodoForm


# Create your views here.

def index(request):
    todo_list = TODO.objects.order_by('id')

    form = TodoForm()

    context = {'todo_list': todo_list, 'form': form}

    return render(request, 'todo/index.html', context)


@require_POST
def add_todo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        new_todo = TODO(text=request.POST['text'])
        new_todo.save()

    return redirect('index')


def complete_todo(request, todo_id):
    todo = TODO.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('index')


def delete_completed(request):
    TODO.objects.filter(complete__exact=True).delete()

    return redirect('index')


def delete_all(request):
    TODO.objects.all().delete()

    return redirect('index')
