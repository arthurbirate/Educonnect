from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import UserForm, EleveForm, CombinedForm
from .models import Table_Eleve
from Institution.models import Institution

from django.http import HttpResponse

# Create your views here.


def index(request):
    return  HttpResponse(f"Hello, world. You're at the Tenant {request.tenant} index.")
# @login_required
# def dashboard(request):
#     if request.user.is_superuser:
#
#         return render(request, 'Utilisateurs/templates/dashboard_EduConnect.html')
#
#     if request.user.is_staff:
#
#         return render(request, 'Utilisateurs/templates/dashboard.html')
#
#     else:
#         return render(request, 'Utilisateurs/templates/dashboard_eleve.html')
#
#     #
#     # else:
#     #
#     #     eleve = get_object_or_404(Table_Eleve, user=request.user)
#     #     institution = eleve.institution
#     #     context = {'eleve': eleve, 'institution': institution}
#     #     return render(request, 'Utilisateurs/templates/dashboard_eleve.html', context)
#
#
# @csrf_exempt
# def login_view(request):
#     if request.user.is_authenticated:
#         return redirect('Utilisateurs:dashboard')
#     page = 'login'
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#
#         try:
#             user = User.objects.get(username=username)
#         except:
#             print("Invalid username or password")
#
#         user = authenticate(request, username=username, password=password)
#
#         if user is not None:
#             login(request, user)
#             return redirect('utilisateurs:dashboard')
#
#         else:
#             print("Invalid username or password")
#
#     return render(request, "Utilisateurs/templates/login_register.html")
#
#
# def logout_view(request):
#     logout(request)
#     messages.error(request, 'You have been logged out.')
#     return redirect("utilisateurs:login")
#
#
def creer_eleve(request):
    if request.method == 'POST':
        form = CombinedForm(request.POST)
        if form.is_valid():
            # Create User
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name']
            )

            # Create Table_Eleve
            Table_Eleve.objects.create(
                user=user,
                classe=form.cleaned_data['classe'],
                parent=form.cleaned_data['parent'],
                address=form.cleaned_data['address'],
                telephone=form.cleaned_data['telephone'],

            )


    else:
        form = CombinedForm()

    return render(request, 'Utilisateurs/templates/creer_eleve.html', {'form': form})
