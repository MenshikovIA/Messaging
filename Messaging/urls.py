from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

from threads.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('threads.api.urls')),
    re_path('', IndexView.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
