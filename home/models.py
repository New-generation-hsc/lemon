from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class CategoryManager(models.Manager):
    def create_category(self, request, name, color):
        str_color = str(color)
        return self.create(name=name, color=str_color, owner=request.user)

class Category(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=12)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    objects = CategoryManager()

    def __str__(self):
        return self.name


class TagManager(models.Manager):
    def create_tag(self, request, name, color):
        str_color = str(color)
        return self.create(name=name, color=str_color, owner=request.user)


class Tag(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=12)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    objects = TagManager()

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=120)
    create_date = models.DateTimeField(default=timezone.now)
    remind_time = models.DateField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.content