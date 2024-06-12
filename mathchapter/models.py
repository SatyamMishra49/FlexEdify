from django.db import models

# Create your models here.
class MathChapter(models.Model):
    mathchapter_title = models.CharField(max_length=50)
    mathchapter_description = models.TextField()