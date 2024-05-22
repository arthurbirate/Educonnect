from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


# Create your views here.

def dashboard(request):
    if request.user.is_superuser:
        return render(request, 'Utilisateurs/templates/dashboard_EduConnect.html')

    if request.user.is_staff:
        return render(request, 'Utilisateurs/templates/dashboard.html')


@csrf_exempt
def login_view(request):
    if request.user.is_authenticated:
        return redirect('Utilisateurs:dashboard')
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            print("Invalid username or password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('utilisateurs:dashboard')

        else:
            print("Invalid username or password")

    return render(request, "Utilisateurs/templates/login_register.html")


def logout_view(request):
    logout(request)
    messages.error(request, 'You have been logged out.')
    return redirect("utilisateurs:login")
