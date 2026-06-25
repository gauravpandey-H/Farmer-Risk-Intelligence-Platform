from django import forms
from .models import Profit

class ProfitForm(forms.ModelForm):
    class Meta:
        model = Profit
        fields = ['crop', 'seed_cost', 'fertilizer_cost', 'labor_cost', 'other_cost', 'expected_yield', 'selling_price']
        
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user and hasattr(user, 'farmer'):
            self.fields['crop'].queryset = user.farmer.crops.all()
