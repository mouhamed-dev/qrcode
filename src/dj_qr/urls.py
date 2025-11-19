
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('qrcode/2025/admin/', admin.site.urls),
    path('', include('Generator.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)