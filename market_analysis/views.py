from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .services import predict_future_prices

@login_required
def market_dashboard(request):
    crop_filter = request.GET.get('crop', 'Tomato')
    
    analysis = predict_future_prices(crop_filter)
    
    context = {
        'selected_crop': crop_filter,
        'current_price': analysis['current_price'],
        'growth_pct': analysis['growth_pct'],
        'historical_labels': analysis['historical']['labels'],
        'historical_data': analysis['historical']['data'],
        'future_labels': analysis['predictions']['labels'],
        'future_data': analysis['predictions']['data'],
    }
    
    return render(request, 'market_analysis/dashboard.html', context)
