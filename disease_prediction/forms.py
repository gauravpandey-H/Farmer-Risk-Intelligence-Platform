from django import forms
from .models import DiseasePrediction

class DiseasePredictionForm(forms.ModelForm):
    class Meta:
        model = DiseasePrediction
        fields = ['crop', 'image']
