from django.shortcuts import render, redirect

from django.http import HttpResponse
# Create your views here.


from .models import Institution
from .forms import DomainForm, InstitutionForm


def enregistrements(request):
    formulaire_institution = InstitutionForm()
    formulaire_domain = DomainForm()

    sufffix = '.educonnect.com'

    if request.method == 'POST':
        formulaire_institution = InstitutionForm(request.POST)
        formulaire_domain = DomainForm(request.POST)

        if formulaire_institution.is_valid() and formulaire_domain.is_valid():
            tenant = formulaire_institution.save()

            domain = formulaire_domain.save(commit=False)
            domain.domain += sufffix
            domain.tenant = tenant
            domain.save()




        else:
            institution = InstitutionForm()
            domain = DomainForm()

    context = {"formulaire_institution": formulaire_institution,"formulaire_domain":formulaire_domain}
    return render(request, 'Institution/templates/creer_institution.html',context)
