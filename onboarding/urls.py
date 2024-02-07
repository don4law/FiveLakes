from django.urls import include, path, re_path
from . import views

urlpatterns = [
    path('', views.onboarding_view, name="onboarding"),
    path('onboard_complete/<pk>/', views.onboard_complete, name="onboard_complete"),
]