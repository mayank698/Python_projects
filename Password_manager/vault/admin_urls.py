from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.admin_user_list, name='admin_user_list'),
    path('users/<int:user_id>/delete/', views.admin_delete_user, name='admin_delete_user'),
] 