from django.db import models

# Create your models here.
class Task(models.Model):
    task_name=models.CharField(max_length=100)
    task_desc=models.TextField(max_length=200)
    date=models.DateTimeField(auto_now=True)
    completed=models.BooleanField(default=False)
    image=models.ImageField(upload_to='Images/',default="Image/None/Noimg.jpg")