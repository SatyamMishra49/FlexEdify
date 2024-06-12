from django.db import models

# Create your models here.
class Chapter(models.Model):
    chapter_title = models.CharField(max_length=30)
    chapter_description = models.TextField()