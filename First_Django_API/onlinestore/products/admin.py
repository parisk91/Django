from django.contrib import admin
from .models import Manufacturer, Product

admin.site.regiister(Manufacturer)
admin.site.regiister(Product)

# Register your models here.
