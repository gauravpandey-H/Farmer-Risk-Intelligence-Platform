from django.db import models
from crops.models import Crop

class Profit(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE, related_name='profits')
    seed_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    fertilizer_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    labor_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    other_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    expected_yield = models.DecimalField(max_digits=10, decimal_places=2, help_text="In kg")
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price per kg")
    total_profit = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        revenue = self.expected_yield * self.selling_price
        expenses = self.seed_cost + self.fertilizer_cost + self.labor_cost + self.other_cost
        self.total_profit = revenue - expenses
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Profit for {self.crop.crop_name}"
