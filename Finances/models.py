import uuid

from django.db import models
from Utilisateurs.models import Table_Eleve


# Create your models here.


class Finance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    frais_scolaire_1 = 'frais scolaire trimestre 1'
    frais_scolaire_2 = 'frais scolaire trimestre 2'
    frais_scolaire_3 = 'frais scolaire trimestre 3'

    frais_scolaire_choices = [
        (frais_scolaire_1, frais_scolaire_1),
        (frais_scolaire_2, frais_scolaire_2),
        (frais_scolaire_3, frais_scolaire_3),

    ]

    statut = models.SmallIntegerField(default=1, choices=[(1, "approuver"), (0, "no approuver")])
    frais_scolaire_choice = models.CharField(max_length=50, choices=frais_scolaire_choices, blank=False, null=False)
    eleve = models.ForeignKey(Table_Eleve, on_delete=models.CASCADE, blank=False, null=False, related_name='finances')
    montants = models.IntegerField(default=0, blank=True, null=True)
    document = models.FileField(upload_to='documents/', blank=False, null=False, default=None)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.eleve.first_name} {self.eleve.last_name}'
