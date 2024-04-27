
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('frontend.urls', namespace='frontend')),
    path('shipment/', include('shipment.urls', namespace='shipment')),
]
urlpatterns += staticfiles_urlpatterns()
