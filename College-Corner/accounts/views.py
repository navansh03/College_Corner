from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from CollegeCorner.views import homepage

@login_required(login_url='login/')
def home(request):
    return homepage(request)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            error_message = 'Invalid login credentials.'
            return render(request, 'accounts/login.html', {'error_message': error_message})
            
        else:
            login(request, user)
            return homepage(request)
            
    else:
        return render(request, 'accounts/login.html')

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return homepage(request)
    
def signup_view(request):
    if request.method == 'POST':
        # Handle signup form submission
        # Extract and save user registration data
        # You can use Django's built-in UserCreationForm or create your own form
        # Redirect to the login page after successful signup
        return homepage(request)
    else:
        return render(request, 'accounts/signup.html')
