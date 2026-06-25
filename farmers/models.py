from django.db import models
from django.contrib.auth.models import User

class Farmer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    village = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    land_size = models.DecimalField(max_digits=6, decimal_places=2, help_text="In acres")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
