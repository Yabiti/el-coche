from django.db import models

# Create your models here.
class Car(models.Model):
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
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Sale(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sale_date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.car} to {self.customer} on {self.sale_date}"