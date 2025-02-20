from django.db import models

# Create your models here.
class Cars(models.Model):
    title = models.CharField(max_length=150)
    make = models.CharField(max_length=150)
    model = models.CharField(max_length=150)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    content = models.TextField()
    image = models.ImageField(upload_to='car/')
    published_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.make} {self.model} {self.year}"

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    emial = models.EmailField()
    phone_number = models.CharField(max_length=15)