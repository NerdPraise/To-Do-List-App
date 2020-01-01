from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="images/avatar")
    memo = models.TextField(max_length=12000)
    def __str__(self):
        return self.user.username

class Category(models.Model):
    category_name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural ="Categories"

    def __str__(self):
        return self.category_name

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateField()
    due_date = models.DateField()
    todo_text = models.CharField(max_length=200)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created"] #orders the the listing of the objects
    def __str__(self):
       return self.user.username

class CompletedList(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    completed_text = models.CharField(max_length=200)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.completed_text

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()