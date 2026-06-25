from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .services import get_weather_data, get_forecast

@login_required
def weather_dashboard(request):
    # Try to get farmer's village/district for location
    location = "Farm Location"
    if hasattr(request.user, 'farmer'):
        location = f"{request.user.farmer.village}, {request.user.farmer.district}"
        
    current_weather = get_weather_data(location)
    forecast = get_forecast(location)
    
    return render(request, 'weather/dashboard.html', {
        'current_weather': current_weather,
        'forecast': forecast
    })
