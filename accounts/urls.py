from django.urls import path, include
# Import the homepage view from the 'accounts' app
from accounts.views import homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/sensor/', include('sensor.urls')),
    path('api/accounts/', include('accounts.urls')),
    path('api/crop_monitoring/', include('crop_monitoring.urls')),
    path('api/recommendation/', include('recommendation.urls')),
    path('', homepage, name='homepage'),  # Root URL
]
