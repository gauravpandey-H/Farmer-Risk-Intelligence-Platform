import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta

from .models import MarketPrice

def predict_future_prices(crop_name):
    # Fetch historical data from the connected SQLite database
    records = MarketPrice.objects.filter(crop_name__icontains=crop_name).order_by('date')
    
    if len(records) < 2:
        return {
            'historical': {'labels': [], 'data': []},
            'predictions': {'labels': [], 'data': []},
            'current_price': 0,
            'growth_pct': 0
        }
        
    dates = [datetime.combine(r.date, datetime.min.time()) for r in records]
    prices = [float(r.price_per_kg) for r in records]
    
    df = pd.DataFrame({'date': dates, 'price': prices})
    df['ordinal_date'] = df['date'].map(datetime.toordinal)
    
    X = df[['ordinal_date']]
    y = df['price']
    
    # Train Linear Regression Model
    model = LinearRegression()
    model.fit(X, y)
    
    # Predict next 3 months
    future_dates = [datetime.now() + timedelta(days=x*30) for x in range(1, 4)]
    future_ordinal = pd.DataFrame({'ordinal_date': [d.toordinal() for d in future_dates]})
    predictions = model.predict(future_ordinal)
    
    historical_labels = [d.strftime('%b %Y') for d in dates]
    future_labels = [d.strftime('%b %Y') for d in future_dates]
    
    return {
        'historical': {
            'labels': historical_labels,
            'data': [round(p, 2) for p in prices]
        },
        'predictions': {
            'labels': future_labels,
            'data': [round(p, 2) for p in predictions]
        },
        'current_price': round(prices[-1], 2),
        'growth_pct': round(((predictions[-1] - prices[-1]) / prices[-1]) * 100, 2)
    }
