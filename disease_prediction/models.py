from django.db import models

class DiseasePrediction(models.Model):
    CROP_CHOICES = [
        ('Tomato', 'Tomato'),
        ('Potato', 'Potato'),
        ('Rice', 'Rice'),
    ]
    crop = models.CharField(max_length=50, choices=CROP_CHOICES, default='Tomato')
    image = models.ImageField(upload_to='disease_images/')
    disease_name = models.CharField(max_length=100)
    confidence = models.DecimalField(max_digits=5, decimal_places=2)
    recommended_solution = models.TextField()
    prediction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.disease_name} on {self.crop}"
