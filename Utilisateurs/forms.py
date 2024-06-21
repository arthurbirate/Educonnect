from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from  django.contrib.auth.models import User
from django import forms
from .models import Table_Eleve, Table_Parent
from Institution.models import Classe, Institution


class EleveForm(ModelForm):
    class Meta:
        model = Table_Eleve
        fields = ['address', 'telephone', 'classe', 'parent']


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1','password2', 'first_name', 'last_name']


