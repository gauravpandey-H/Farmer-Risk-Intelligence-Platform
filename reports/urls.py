from django.urls import path
from . import views

urlpatterns = [
    path('', views.reports_dashboard, name='reports_dashboard'),
    path('export/csv/crops/', views.export_crops_csv, name='export_crops_csv'),
    path('export/pdf/farmer/', views.export_farmer_pdf, name='export_farmer_pdf'),
]
