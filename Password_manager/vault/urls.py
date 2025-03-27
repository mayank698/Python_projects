from django.urls import path, include
from . import views

urlpatterns = [
    # User routes
    path('', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('password/new/', views.password_create, name='password_create'),
    path('password/<uuid:pk>/edit/', views.password_edit, name='password_edit'),
    path('password/<uuid:pk>/delete/', views.password_delete, name='password_delete'),
    path('search/', views.search_passwords, name='search_passwords'),
    path('account/delete/', views.delete_account, name='delete_account'),
    
    # Admin routes (separate from user routes)
    path('admin/', include('vault.admin_urls')),
] 