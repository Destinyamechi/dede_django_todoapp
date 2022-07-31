from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length = 150)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=50, null= True, blank=True)

    def __str__(self):
        return f"{self.title}"
     

 