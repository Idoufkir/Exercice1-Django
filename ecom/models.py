from django.db import models

from django.db import models


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    reference = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    description = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Variant(models.Model):
    id = models.AutoField(primary_key=True)
    specification = models.CharField(max_length=100)
    sku = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    product = models.ForeignKey(Product, related_name="variants", on_delete=models.CASCADE)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.specification
