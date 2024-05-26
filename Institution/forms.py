from django.forms import ModelForm

from Utilisateurs.models import User
from .models import Institution


class InstitutionForm(ModelForm):
    class Meta:
        model = Institution
        fields = ['name', 'promotion', 'contact_number', 'address']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'is_staff', ]
