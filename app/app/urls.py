from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView
)
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/',
         SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger'),
    path('api/redoc/',
         SpectacularRedocView.as_view(url_name='schema'),
         name='redoc'),
    path('api/user/', include('user.urls')),
    path('api/recipe/', include('recipe.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
