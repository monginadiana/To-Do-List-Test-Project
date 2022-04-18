from django.db import models
import datetime as dt

# Create your models here.
class ToDo(models.Model):
    name = models.CharField(max_length=30)
    description= models.CharField(max_length=30)
    category= models.CharField(max_length=30)
    complete = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def save_ToDo(self):
        self.save()
    
    def update_ToDo(self):
        self.save()

    def __str__(self):
        return self.name

