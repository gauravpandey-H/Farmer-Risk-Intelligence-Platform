from django.db import models

class MarketPrice(models.Model):
    crop_name = models.CharField(max_length=100)
    market_name = models.CharField(max_length=100)
    price_per_kg = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.crop_name} at {self.market_name} - {self.date}"
