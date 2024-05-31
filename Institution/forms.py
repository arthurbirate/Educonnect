from django.forms import ModelForm
from django import forms

from django.contrib.auth.models import User
# from Utilisateurs.models import User
from .models import Institution, Domain


class InstitutionForm(ModelForm):
    class Meta:
        model = Institution
        fields = ['schema_name', 'name', 'promotion', 'contact_number', 'address']


class DomainForm(ModelForm):
    class Meta:
        model = Domain
        fields = ['domain','is_primary']

#
# class UserForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password', 'is_staff', ]
