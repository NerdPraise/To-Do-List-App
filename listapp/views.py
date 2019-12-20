from django.shortcuts import render
from django.utils import timezone
from .models import Todo
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    todo_items = Todo.objects.all().order_by("-added_date")
    context = {
        "todo_items" : todo_items
    }
    return render(request, "listapp/index.html", context)

def add_todo(request):
    current_date = timezone.now()
    content = request.POST["content"]
    Todo.objects.create(added_date=current_date, text=content)
    return HttpResponseRedirect("/")

@csrf_exempt
def delete_todo(request, todo_id):
    item = Todo.objects.get(pk=todo_id)
    item.delete()
    return HttpResponseRedirect("/")
