from django.db import models
from brand.models import Brand
from django.contrib.auth.models import User

class Car(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='car/uploads', blank=True)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.IntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='cars')
    purchased_by = models.ManyToManyField(User, related_name='purchased_cars', blank=True)

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Commented by {self.name}"