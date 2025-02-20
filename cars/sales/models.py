from django.db import models

# Create your models here.
class Cars(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True)
