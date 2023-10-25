from django.contrib import admin
from .models import add_task, todo

# Register your models here.
admin.site.register(add_task)
admin.site.register(todo)