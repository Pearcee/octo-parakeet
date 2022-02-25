from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    return render(request, "todo/index.html", {"todo_list": todos})
    # return HttpResponse("Hello World!!")


@require_http_methods(["POST"])
def add(request):
    # if request.method == "POST":
    title = request.POST["title"]
    todo = Todo(title=title)
    todo.save()
    return redirect("index")


def update(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.complete = not todo.complete
    todo.save()
    return redirect("index")


def delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect("index")