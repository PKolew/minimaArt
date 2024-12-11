from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('', include('minima_art.web.urls')),
    path('gallery/', include('minima_art.picture_products.urls')),
    path('products/', include('minima_art.picture_products.urls')),
    path('users/', include('minima_art.users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
