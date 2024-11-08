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
    path('edit_task/<pk>/', views.edit_task, name="edit_task"),
    path('delete_task/<pk>/', views.delete_task, name="delete_task"),
    path('add_metric/<pk>/', views.add_metric, name="add_metric"),
    path('edit_metric/<employee>/<pk>/', views.edit_metric, name="edit_metric"),
    path('add_hr/<pk>/', views.add_hr, name="add_hr"),
    path('edit_hr/<employee>/<pk>/', views.edit_hr, name="edit_hr"),
    path('delete_metric/<pk>/', views.delete_metric, name="delete_metric"),
    path('delete_QA/<employee>/<pk>/', views.delete_QA, name="delete_QA"),
    path('delete_note/<employee>/<pk>/', views.delete_note, name="delete_note"),
    path('delete_call/<employee>/<pk>/', views.delete_call, name="delete_call"),
    path('add_issue/<pk>/', views.add_issue, name="add_issue"),
    path('add_issue/<employee>/<pk>/', views.edit_issue, name="edit_issue"),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)