from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('', views.attorney_view, name="attorneys"),
    path('attorney_data/<pk>/', views.attorney_data, name="attorney_data"),
    path('add_attorney_more_onboarding/<pk>/', views.add_attorney_more_onboarding, name="add_attorney_more_onboarding"),
    path('edit_attorney_profile/<pk>/', views.edit_attorney_profile, name="edit_attorney_profile"),
    path('add_note/<pk>', views.add_note, name="add_note"),
    path('edit_note/<employee>/<pk>/', views.edit_note, name="edit_note"),
    path('add_call/<pk>/', views.add_call, name="add_call"),
    path('edit_call/<employee>/<pk>/', views.edit_call, name="edit_call"),
    path('add_coaching/<pk>/', views.add_coaching, name="add_coaching"),
    path('edit_coaching/<employee>/<pk>/', views.edit_coaching, name="edit_coaching"),
    path('add_todo/<pk>/', views.add_todo, name="add_todo"),
    path('edit_task/<employee>/<pk>/', views.edit_task, name="edit_task"),
    path('delete_task/<pk>/', views.delete_task, name="delete_task"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)