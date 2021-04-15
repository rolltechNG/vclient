from django.db import models


# Create your models here.

class Price(models.Model):
    """
    A model to store fixed prices for the services
    (e.g nin, demo, phone)
    """
    nin_price = models.DecimalField(max_digits=10, decimal_places=2, default=1000.00, blank=True, null=True)
    phone_price = models.DecimalField(max_digits=10, decimal_places=2, default=1000.00, blank=True, null=True)
    demo_price = models.DecimalField(max_digits=10, decimal_places=2, default=1000.00, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Prices"

    def __str__(self):
        return f"{self.nin_price} {self.phone_price} {self.demo_price}"
