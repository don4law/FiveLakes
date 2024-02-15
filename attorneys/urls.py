from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('', views.attorney_view, name="attorneys"),
    path('attorney_data/<pk>/', views.attorney_data, name="attorney_data"),
    path('edit_attorney_QA/<pk>/', views.edit_attorney_QA, name="edit_attorney_QA"),
    path('add_attorney_more_onboarding/<pk>/', views.add_attorney_more_onboarding, name="add_attorney_more_onboarding"),
    path('edit_attorney_profile/<pk>/', views.edit_attorney_profile, name="edit_attorney_profile"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)