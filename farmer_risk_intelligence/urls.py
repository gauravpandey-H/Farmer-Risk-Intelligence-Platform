from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('accounts/', include('accounts.urls')),
    path('farmers/', include('farmers.urls')),
    path('crops/', include('crops.urls')),
    path('weather/', include('weather.urls')),
    path('disease-prediction/', include('disease_prediction.urls')),
    path('market-analysis/', include('market_analysis.urls')),
    path('profit-calculator/', include('profit_calculator.urls')),
    path('reports/', include('reports.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
