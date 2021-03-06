from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Todo, Category, CompletedList, User
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .forms import SignUpForm
from django.contrib.auth import views, login, authenticate


# Create your views here.
def home(request):
    current_date = timezone.now()
    user_items = User.objects.all()
    categories = Category.objects.all().order_by("category_name")
    context = {
            "current_date": current_date,
            "user_items": user_items,
            "categories" : categories,
        }
    return render(request, "listapp/index.html", context)

def save_memo(request):
    user = request.user
    if request.POST:
        memo = request.POST["memo"]
        user.userprofile.memo = memo
        user.save()
    return redirect("/")


def add_todo(request):
    current_date = timezone.now()
    content = request.POST["content"]
    date = request.POST["date"]
    category_chosen = request.POST["category"]
    user = request.user
    user.todo_set.create(created=current_date, due_date=date, todo_text=content, category_name=Category.objects.get(category_name=category_chosen))
    return HttpResponseRedirect("/")

@csrf_exempt
def delete_todo(request, todo_id):
    item = Todo.objects.get(pk=todo_id)
    item.delete()
    return HttpResponseRedirect("/")

@csrf_exempt
def completed_todo(request, todo_id):
    item = Todo.objects.get(pk=todo_id)
    user = request.user
    user.completedlist_set.create(completed_text=item.todo_text, category_name=item.category_name)
    item.delete()
    return HttpResponseRedirect("/")

def register(request):
    form = SignUpForm(request.POST, request.FILES)
    if request.POST:
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.userprofile.avatar = form.cleaned_data["image"]
            user.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("home")
    else:
        form = SignUpForm()
    context = {"form":form}
    return render(request, "registration/register.html", context)

class Login(views.LoginView):
    redirect_field_name = "home"

def logout(request):
    return views.logout_then_login(request)

