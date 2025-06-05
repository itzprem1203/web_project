from django.shortcuts import render, redirect
from .models import UserLogin
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        print('your data from frontend is this :',username,password)

        try:
            UserLogin.objects.update_or_create(
                username=username,
                defaults={'password': password}
            )
        except UserLogin.DoesNotExist:
            messages.error(request, "Invalid credentials")

        try:
            user = UserLogin.objects.get(username=username, password=password)
            return render(request, 'app/welcome.html', {'user': user})
        except UserLogin.DoesNotExist:
            messages.error(request, "Invalid credentials")
    
    return render(request, 'app/login.html')
