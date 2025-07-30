from django.db import models
from django.urls import reverse

class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("product:item_detail", args=[str(self.id)])