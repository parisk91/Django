from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=60)
    location = models.CharField(max_length=60)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=60)
    photo = models.FloatField()
    shipping_cost = models.FloatField()
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name
