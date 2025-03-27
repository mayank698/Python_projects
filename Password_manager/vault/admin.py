from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Password

@admin.register(Password)
class PasswordAdmin(admin.ModelAdmin):
    list_display = ('website', 'username', 'user', 'created_at', 'updated_at')
    search_fields = ('website', 'username', 'notes')
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('id', 'created_at', 'updated_at')

# Unregister the default User admin
admin.site.unregister(User)

# Register User with custom admin
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('-date_joined',)
    actions = ['delete_selected']
