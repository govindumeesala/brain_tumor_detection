from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .forms import ImageUploadForm
from .utils import handle_uploaded_image 

def home_view(request):
    return render(request, 'detection/home.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('upload_image')
        messages.error(request, "Give correct credentials.")
    else:
        form = UserCreationForm()
    return render(request, 'detection/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful.")
                return redirect('upload_image')
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'detection/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")  
    return redirect('login')

# Upload Image view for tumor detection
def upload_image_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            result = handle_uploaded_image(image)  # Calls tumor detection logic
            return render(request, 'detection/result.html', {'result': result}) 
    else:
        form = ImageUploadForm()
    return render(request, 'detection/upload_image.html', {'form': form})
