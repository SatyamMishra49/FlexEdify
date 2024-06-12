from django.db import models

# Create your models here.
class ScienceChapter(models.Model):
    sciencechapter_title = models.CharField(max_length=50)
    sciencechapter_description = models.TextField()