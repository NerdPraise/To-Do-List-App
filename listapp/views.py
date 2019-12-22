from django.shortcuts import render
from django.utils import timezone
from .models import Todo, Category, CompletedList
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def home(request):
    current_date = timezone.now()
    todo_items = Todo.objects.all()
    categories = Category.objects.all().order_by("category_name")
    completelist = CompletedList.objects.all()
    context = {
        "current_date": current_date,
        "todo_items" : todo_items,
        "categories" : categories,
        "completelist": completelist,
    }
    return render(request, "listapp/index.html", context)

def add_todo(request):
    current_date = timezone.now()
    content = request.POST["content"]
    date = request.POST["date"]
    category_chosen = request.POST["category"]
    print(date)
    Todo.objects.create(created=current_date, due_date=date, todo_text=content, category_name=Category.objects.get(category_name=category_chosen))
    return HttpResponseRedirect("/")

@csrf_exempt
def delete_todo(request, todo_id):
    item = Todo.objects.get(pk=todo_id)
    print(item.due_date)
    return HttpResponseRedirect("/")

@csrf_exempt
def completed_todo(request, todo_id):
    item = Todo.objects.get(pk=todo_id)
    CompletedList.objects.create(completed_text=item.todo_text, category_name=item.category_name)
    item.delete()
    return HttpResponseRedirect("/")
