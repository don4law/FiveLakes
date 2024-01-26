from django.urls import include, path, re_path
from . import views

urlpatterns = [
    path('states', views.states_view, name="states"),
    path('add_states', views.add_states, name="add_states"),
    path('edit_state/<pk>/', views.edit_state, name="edit_state"),
]