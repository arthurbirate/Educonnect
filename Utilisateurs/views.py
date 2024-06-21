from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import UserForm, EleveForm
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

    if request.user in Table_Professeur.objects.all():
        return render(request, 'Utilisateurs/templates/dashboard_enseignent.html')

    else:
        eleve = get_object_or_404(Table_Eleve, user=request.user)
        context = {'eleve': eleve}
        return render(request, 'Utilisateurs/templates/dashboard_eleve.html', context)


@csrf_exempt
def loginUser(request):
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

        # form = CombinedForm(request.POST)
        # if form.is_valid():
        #     # Create User
        #     user = User.objects.create_user(
        #         username=form.cleaned_data['username'],
        #         password=form.cleaned_data['password'],
        #         first_name=form.cleaned_data['first_name'],
        #         last_name=form.cleaned_data['last_name']
        #     )
        #
        #     # Create Table_Eleve
        #     Table_Eleve.objects.create(
        #         user=user,
        #         first_name=User.objects.get(username=form.cleaned_data['first_name']),
        #         last_name=User.objects.get(username=form.cleaned_data['last_name']),
        #         classe=form.cleaned_data['classe'],
        #         parent=form.cleaned_data['parent'],
        #         address=form.cleaned_data['address'],
        #         telephone=form.cleaned_data['telephone'],
        #
        #
        #     )


    else:
        formulaire_eleve = EleveForm()
        formulaire_utilisateur = UserForm()

    context = {'formulaire_eleve': formulaire_eleve, 'formulaire_utilisateur': formulaire_utilisateur}

    return render(request, 'Utilisateurs/templates/creer_eleve.html', context)
