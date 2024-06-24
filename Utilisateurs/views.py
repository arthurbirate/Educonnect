from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import UserForm, EleveForm, ProfesseurForm
from .models import Table_Eleve, Table_Professeur
from Institution.models import Institution

from django.http import HttpResponse


# Create your views here.


def index(request):
    return HttpResponse(f"Hello, world. You're at the Tenant {request.tenant} index.")


@login_required
def dashboard(request):
    if request.user.is_superuser:
        return render(request, 'Utilisateurs/templates/dashboard_EduConnect.html')

    if request.user.is_staff:
        return render(request, 'Utilisateurs/templates/dashboard.html')


    else:
        eleve = get_object_or_404(Table_Eleve, user=request.user)
        context = {'eleve': eleve}
        return render(request, 'Utilisateurs/templates/dashboard_eleve.html', context)


def dashboard_professeur(request):
    professeur = get_object_or_404(Table_Professeur, user=request.user)
    context = {'professeur': professeur}
    return render(request, 'Utilisateurs/templates/dashboard_enseignent.html', context)


@csrf_exempt
def loginUser(request):
    # if request.user.is_authenticated:
    #     return redirect('Utilisateurs:dashboard')
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
            if hasattr(user, 'professeur'):
                return redirect('Utilisateurs:dashboard_professeur')
            return redirect('utilisateurs:dashboard')

        else:
            print("Invalid username or password")

    return render(request, "Utilisateurs/templates/login_register.html")


def logoutUser(request):
    logout(request)
    messages.error(request, 'You have been logged out.')
    return redirect("utilisateurs:login")


def creer_eleve(request):
    formulaire_eleve = EleveForm()
    formulaire_utilisateur = UserForm()
    if request.method == 'POST':
        formulaire_eleve = EleveForm(request.POST)
        formulaire_utilisateur = UserForm(request.POST)

        if formulaire_eleve.is_valid() and formulaire_utilisateur.is_valid():
            utilisateur = formulaire_utilisateur.save()
            eleve = formulaire_eleve.save(commit=False)

            eleve.user = utilisateur

            eleve.first_name = utilisateur.first_name
            eleve.last_name = utilisateur.last_name

            eleve.save()

    else:
        formulaire_eleve = EleveForm()
        formulaire_utilisateur = UserForm()

    context = {'formulaire_eleve': formulaire_eleve, 'formulaire_utilisateur': formulaire_utilisateur}

    return render(request, 'Utilisateurs/templates/creer_eleve.html', context)


def creer_professeur(request):
    formulaire_professeur = ProfesseurForm()
    formulaire_utilisateur = UserForm()

    if request.method == 'POST':
        formulaire_professeur = ProfesseurForm(request.POST)
        formulaire_utilisateur = UserForm(request.POST)

        if formulaire_professeur.is_valid() and formulaire_utilisateur.is_valid():
            utilisateur = formulaire_utilisateur.save()
            professeur = formulaire_professeur.save(commit=False)
            professeur.user = utilisateur
            professeur.first_name = utilisateur.first_name
            professeur.last_name = utilisateur.last_name
            professeur.save()

    else:
        formulaire_professeur = ProfesseurForm()
        formulaire_utilisateur = UserForm()

    context = {'formulaire_professeur': formulaire_professeur, 'formulaire_utilisateur': formulaire_utilisateur}

    return render(request, 'Utilisateurs/templates/creer_professeur.html', context)
