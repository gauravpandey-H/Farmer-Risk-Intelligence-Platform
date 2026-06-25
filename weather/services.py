import random

def get_weather_data(location="Unknown"):
    # Simulated weather data since we don't have an API key right now
    return {
        'location': location,
        'temperature': random.randint(15, 35),
        'humidity': random.randint(40, 90),
        'rainfall': random.randint(0, 20),
        'wind_speed': random.randint(5, 25),
        'condition': random.choice(['Sunny', 'Cloudy', 'Rainy', 'Clear'])
    }

def get_forecast(location="Unknown"):
    # Simulated 7-day forecast
    forecast = []
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    for day in days:
        forecast.append({
            'day': day,
            'high': random.randint(25, 35),
            'low': random.randint(15, 24),
            'condition': random.choice(['Sunny', 'Cloudy', 'Rainy'])
        })
    return forecast
