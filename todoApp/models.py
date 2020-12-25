from django.db import models

# Create your models here.
#create the models
class Todo(models.Model):
  content = models.TextField()