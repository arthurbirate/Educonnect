from django.shortcuts import render, redirect

# Create your views here.


from .models import Institution
from .forms import UserForm, InstitutionForm


def createInstitution(request):
    formUser = UserForm()
    formInstitution = InstitutionForm()
    if request.method == 'POST':
        formUser = UserForm(request.POST)
        formInstitution = InstitutionForm(request.POST)

        if formInstitution.is_valid() and formUser.is_valid():
            formInstitution.save()
            formUser.save()

    context = {"formUser": formUser, "formInstitution": formInstitution}
    return render(request, 'Institution/templates/creer_institution.html', context)
