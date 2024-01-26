from django.urls import include, path, re_path
from . import views

urlpatterns = [
    path('', views.onboarding_view, name="onboarding"),
]