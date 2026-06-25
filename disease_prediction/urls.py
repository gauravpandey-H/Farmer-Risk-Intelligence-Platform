from django.urls import path
from . import views

urlpatterns = [
    path('', views.predict, name='predict_disease'),
    path('history/', views.prediction_history, name='prediction_history'),
]
