from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self) -> str:
        return f'{self.name} {self.description}'

class ProductPet(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=100, null=False, blank=False)
    price = models.DecimalField(max_digits=9, decimal_places=2, null=False, blank=False)
    weight = models.DecimalField(max_digits=9, decimal_places=3, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return f'{self.name} {self.price} {self.created_at}'
