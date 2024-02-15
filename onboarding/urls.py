from django.urls import include, path, re_path
from . import views

urlpatterns = [
    path('', views.onboarding_view, name="onboarding"),
    path('onboarding_detail/<pk>/', views.onboarding_detail, name="onboarding_detail"),
    path('onboarding_detail2/<pk>/', views.onboarding_detail2, name="onboarding_detail2"),
    path('onboard_complete/<pk>/', views.onboard_complete, name="onboard_complete"),
    path('onboarding_text/<pk>/', views.onboarding_text, name="onboarding_text"),
]