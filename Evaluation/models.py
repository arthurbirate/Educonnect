import uuid

from django.db import models
from Institution.models import Classe
from Utilisateurs.models import Table_Eleve





class Devoir(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    titre = models.CharField(max_length=200, unique=True, blank=False, null=False)
    cour = models.ForeignKey('Cour', on_delete=models.CASCADE,  blank=False, null=False, default=None)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, blank=False, null=False, default=None)
    description = models.TextField(blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    file = models.FileField(blank=False, null=False, upload_to='devoir/')

    def __str__(self):
        return self.titre


class Cour(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    classe = models.ManyToManyField(Classe, blank=True, related_name='cours', null=False)
    name = models.CharField(max_length=200, unique=True, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Presence(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cour = models.ForeignKey(Cour, on_delete=models.CASCADE, blank=True, null=True, related_name='presences')
    eleve = models.ForeignKey(Table_Eleve, on_delete=models.CASCADE, blank=True, null=True, related_name='presences')
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, blank=True, null=True, related_name='presences')
    date = models.DateField(blank=False, null=False)

    def __str__(self):
        return str(self.date)


class devoir_soumission(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    eleve = models.ForeignKey(Table_Eleve, on_delete=models.CASCADE, blank=True,default=None, null=True, related_name='soumissions')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.eleve
