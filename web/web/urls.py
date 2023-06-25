from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from shop.views import *
from web import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls'))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path("__debug__/", include("debug_toolbar.urls")),
    ] + urlpatterns


if settings.DEBUG: #Тільки для режиму відладки
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound
