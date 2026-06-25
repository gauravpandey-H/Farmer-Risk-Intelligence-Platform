from django import forms
from .models import Crop

class CropForm(forms.ModelForm):
    class Meta:
        model = Crop
        fields = ['farmer', 'crop_name', 'soil_type', 'land_area', 'sowing_date', 'fertilizer_used', 'status']
        widgets = {
            'sowing_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_land_area(self):
        land_area = self.cleaned_data.get('land_area')
        if land_area <= 0:
            raise forms.ValidationError("Land Area must be greater than 0.")
        return land_area
