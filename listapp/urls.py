from . import views
from django.urls import path

urlpatterns=[
    path("", views.home, name="home"),
    path("add_todo", views.add_todo, name="add"),
    path("delete_todo/<int:todo_id>", views.delete_todo, name="delete"),
    path("completed_todo/<int:todo_id>", views.completed_todo, name="completed"),
    path("register", views.register, name="register"),
    path("logout", views.Logout.as_view(), name="logout"),
    path("login", views.Login.as_view(), name="login"),
]