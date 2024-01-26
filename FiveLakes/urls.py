"""
FiveLakes settings.url
"""
from django.contrib import admin
from django.urls import include, path, re_path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('managers/', include('managers.urls')),
    path('managers/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('states/', include('states.urls')),
    path('attorneys/', include('attorneys.urls')),
    path('recruiting/', include('recruiting.urls')),
    path('onboarding/', include('onboarding.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
