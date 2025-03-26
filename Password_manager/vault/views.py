from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PasswordForm, SignUpForm, CustomAuthenticationForm
from .models import Password
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import JsonResponse

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'vault/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'vault/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')

@login_required
def dashboard(request):
    passwords = Password.objects.filter(user=request.user).order_by('-updated_at')
    return render(request, 'vault/dashboard.html', {'passwords': passwords})

@login_required
def password_create(request):
    if request.method == 'POST':
        form = PasswordForm(request.POST, user=request.user)
        if form.is_valid():
            password = form.save(commit=False)
            password.user = request.user
            password.save()
            messages.success(request, 'Password saved successfully!')
            return redirect('dashboard')
    else:
        form = PasswordForm(user=request.user)
    return render(request, 'vault/password_form.html', {'form': form, 'action': 'Create'})

@login_required
def password_edit(request, pk):
    password = get_object_or_404(Password, pk=pk, user=request.user)
    if request.method == 'POST':
        form = PasswordForm(request.POST, instance=password, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password updated successfully!')
            return redirect('dashboard')
    else:
        form = PasswordForm(instance=password, user=request.user)
    return render(request, 'vault/password_form.html', {'form': form, 'action': 'Edit'})

@login_required
def password_delete(request, pk):
    password = get_object_or_404(Password, pk=pk, user=request.user)
    if request.method == 'POST':
        password.delete()
        messages.success(request, 'Password deleted successfully!')
        return redirect('dashboard')
    return render(request, 'vault/password_confirm_delete.html', {'password': password})

@login_required
def search_passwords(request):
    query = request.GET.get('q', '')
    
    if query:
        passwords = Password.objects.filter(
            Q(website__icontains=query) | 
            Q(username__icontains=query) | 
            Q(notes__icontains=query),
            user=request.user
        ).order_by('-updated_at')
    else:
        passwords = Password.objects.filter(user=request.user).order_by('-updated_at')
    
    # Return JSON for API requests
    if request.GET.get('format') == 'json':
        password_data = [
            {
                'id': str(p.id),
                'website': p.website,
                'username': p.username,
                'updated_at': p.updated_at.isoformat()
            } for p in passwords
        ]
        return JsonResponse(password_data, safe=False)
    
    # Regular HTML response
    return render(request, 'vault/dashboard.html', {'passwords': passwords, 'query': query})
