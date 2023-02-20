from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from thebeerblog import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')))
