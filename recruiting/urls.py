from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('', views.recruiting_view, name="recruiting"),
    path('add_applicant', views.add_applicant, name="add_applicant"),
    path('edit_applicant/<pk>/', views.edit_applicant, name="edit_applicant"),
    path('applicant_delete/<pk>/', views.applicant_delete, name="applicant_delete"),
    path('applicant_detail/<pk>/', views.applicant_detail, name="applicant_detail"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)