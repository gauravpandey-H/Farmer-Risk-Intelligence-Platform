from django.db import models
from farmers.models import Farmer

class Crop(models.Model):
    STATUS_CHOICES = [
        ('Growing', 'Growing'),
        ('Harvested', 'Harvested'),
        ('Diseased', 'Diseased')
    ]
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, related_name='crops')
    crop_name = models.CharField(max_length=100)
    soil_type = models.CharField(max_length=100)
    land_area = models.DecimalField(max_digits=6, decimal_places=2, help_text="In acres")
    sowing_date = models.DateField()
    fertilizer_used = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.crop_name} - {self.farmer.name}"
