from django.urls import path
from . import views

urlpatterns = [
    path('', views.market_dashboard, name='market_dashboard'),
]
