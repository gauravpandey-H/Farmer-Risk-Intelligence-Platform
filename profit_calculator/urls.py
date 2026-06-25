from django.urls import path
from . import views

urlpatterns = [
    path('', views.profit_dashboard, name='profit_dashboard'),
    path('add/', views.add_profit_estimate, name='add_profit_estimate'),
]
