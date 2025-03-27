from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Password

class PasswordForm(forms.ModelForm):
    class Meta:
        model = Password
        fields = ['website', 'username', 'password', 'notes']
        widgets = {
            'password': forms.PasswordInput(render_value=True),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.instance_id = kwargs.get('instance', None)
        if self.instance_id:
            self.instance_id = self.instance_id.id
        super().__init__(*args, **kwargs)
    
    def clean_website(self):
        website = self.cleaned_data.get('website')
        if self.user:
            # Check if password exists for this website
            existing = Password.objects.filter(user=self.user, website__iexact=website)
            # Exclude current instance if editing
            if self.instance_id:
                existing = existing.exclude(id=self.instance_id)
            
            if existing.exists():
                raise forms.ValidationError("You already have a password saved for this website. Please edit the existing entry instead.")
        return website

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError("A user with this username already exists. Please choose a different username.")
        return username

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})) 