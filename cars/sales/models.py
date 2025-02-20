from django.db import models

# Create your models here.
class Cars(models.Model):
    title = models.CharField(max_length=150)
    make = models.CharField(max_length=150)
    model = models.CharField(max_length=150)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True)
    published_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title