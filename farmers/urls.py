from django.urls import path
from . import views

urlpatterns = [
    path('', views.FarmerListView.as_view(), name='farmer_list'),
    path('<int:pk>/', views.FarmerDetailView.as_view(), name='farmer_detail'),
    path('new/', views.FarmerCreateView.as_view(), name='farmer_create'),
    path('<int:pk>/edit/', views.FarmerUpdateView.as_view(), name='farmer_update'),
    path('<int:pk>/delete/', views.FarmerDeleteView.as_view(), name='farmer_delete'),
]
