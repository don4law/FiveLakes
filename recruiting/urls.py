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
    path('applicant_interview1/<pk>/', views.applicant_interview1, name="applicant_interview1"),
    path('int1_decline_text/<pk>/', views.int1_decline_text, name="int1_decline_text"),
    path('applicant_interview2/<pk>/', views.applicant_interview2, name="applicant_interview2"),
    path('applicant_final_step/<pk>/', views.applicant_final_step, name="applicant_final_step"),
    path('int2_decline_text/<pk>/', views.int2_decline_text, name="int2_decline_text"),
    path('offer_letter_text/<pk>/', views.offer_letter_text, name="offer_letter_text"),
    path('create_employee_file/<pk>/', views.create_employee_file, name="create_employee_file"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)