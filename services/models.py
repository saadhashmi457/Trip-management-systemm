from django.db import models

# Create your models here.
class Services(models.Model):
    Services_title=models.CharField(max_length=100)
    Services_detail=models.TextField()

    