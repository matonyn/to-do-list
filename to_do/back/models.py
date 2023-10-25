from django.db import models
import random

# Create your models here.

class todo(models.Model):
    id = models.PositiveIntegerField(default=random.randint(1,10000), primary_key=True)

    def __str__(self) -> str:
        return self.id 
    

class add_task(models.Model):
    id = models.PositiveIntegerField(primary_key=True, default=random.randint(1, 1000))
    name = models.CharField(max_length=500, default="TASK")
    done = models.BooleanField(default=False)
    todo = models.ForeignKey(todo, on_delete=models.CASCADE, default=None)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['done']
