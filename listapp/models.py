from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural ="Categories"

    def __str__(self):
        return self.category_name

class Todo(models.Model):
    created = models.DateTimeField()
    due_date = models.DateTimeField()
    todo_text = models.CharField(max_length=200)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created"] #orders the the listing of the objects
    def __str__(self):
       return self.todo_text



class CompletedList(models.Model):
    completed_text = models.CharField(max_length=200)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.completed_text
