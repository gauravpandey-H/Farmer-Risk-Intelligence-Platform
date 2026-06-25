from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from farmers.models import Farmer
from crops.models import Crop
from profit_calculator.models import Profit

@login_required
def main_dashboard(request):
    context = {
        'total_crops': 0,
        'healthy_crops': 0,
        'diseased_crops': 0,
        'total_profit': 0
    }
    
    if hasattr(request.user, 'farmer'):
        farmer = request.user.farmer
        crops = farmer.crops.all()
        context['total_crops'] = crops.count()
        context['healthy_crops'] = crops.filter(status='Growing').count() # Using Growing as healthy for simplicity
        context['diseased_crops'] = crops.filter(status='Diseased').count()
        
        profits = Profit.objects.filter(crop__in=crops)
        context['total_profit'] = sum([p.total_profit for p in profits if p.total_profit])
        
    return render(request, 'dashboard/main.html', context)
