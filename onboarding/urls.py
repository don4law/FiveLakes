from django.urls import include, path, re_path
from . import views

urlpatterns = [
    path('', views.onboarding_view, name="onboarding"),
    path('onboarding_detail/<pk>/', views.onboarding_detail, name="onboarding_detail"),
    path('onboard_complete/<pk>/', views.onboard_complete, name="onboard_complete"),
]