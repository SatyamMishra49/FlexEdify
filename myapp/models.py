
# Create your models here.
from django.db import models

class Todo(models.Model):
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    c_answer = models.IntegerField()
    topic = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:

        managed = False

        db_table = 'todo'
