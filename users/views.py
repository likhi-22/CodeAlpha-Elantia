from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

User = get_user_model()

@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            return JsonResponse({'success': False, 'message': 'Username already exists.'})
        user = User.objects.create_user(username=username, email=email, password=password)
        return JsonResponse({'success': True, 'message': 'Account created successfully.'})
    return JsonResponse({'success': False, 'message': 'Invalid request.'})

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'success': True, 'message': 'Login successful.'})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid credentials.'})
    return JsonResponse({'success': False, 'message': 'Invalid request.'})

def logout_view(request):
    logout(request)
    return render(request, 'index.html', {'message': 'You have been logged out.'})

def location(request):
    return render(request, 'location.html')
