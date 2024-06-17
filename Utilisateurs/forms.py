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


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name']


# class CombinedForm(forms.Form):
#     username = forms.CharField(max_length=150)
#     password = forms.CharField(widget=forms.PasswordInput)
#     first_name = forms.CharField(max_length=200)
#     last_name = forms.CharField(max_length=200)
#     classe = forms.ModelChoiceField(queryset=Classe.objects.all(), required=False)
#     parent = forms.ModelChoiceField(queryset=Table_Parent.objects.all(), required=False)
#     address = forms.CharField(max_length=50)
#     telephone = forms.CharField(max_length=15, required=False)
