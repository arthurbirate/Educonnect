import uuid

from django.db import models
from Utilisateurs.models import Table_Eleve
from Institution.models import Classe
# from Evaluation.models import Cour


# Create your models here.


class Presence(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    eleve = models.ForeignKey(Table_Eleve, on_delete=models.CASCADE, blank=True, null=True)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, blank=True, null=True)
    # cour = models.ForeignKey(Cour, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return str(self.date)
