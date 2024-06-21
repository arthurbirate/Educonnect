import uuid

from django.db import models

from Utilisateurs.models import Table_Eleve, Table_Professeur


class Evaluation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    titre = models.CharField(max_length=200, unique=True, blank=False, null=False)

    devoir = "devoir"
    examen = "examen"
    interro = "interrogation"

    evaluation_choice = [
        (devoir, devoir),
        (examen, examen),
        (interro, interro),
    ]

    evaluation_type = models.CharField(max_length=200, blank=False, null=False, choices=evaluation_choice, default=None)
    cour = models.OneToOneField('Cour', on_delete=models.CASCADE, blank=False, null=False, default=None,
                                related_name='evaluations')
    classe = models.OneToOneField('Institution.Classe', on_delete=models.CASCADE, blank=False, null=False, default=None,
                                  related_name='evaluations')
    description = models.TextField(blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    file = models.FileField(blank=False, null=False, upload_to='devoir/')
    delais = models.DateTimeField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titre


class Cour(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    classe = models.ManyToManyField('Institution.Classe', blank=True, related_name='cours', null=False)
    name = models.CharField(max_length=200, unique=True, blank=False, null=False)
    description = models.TextField(blank=False, null=False, default=None)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Devoir_Soumission(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    eleve = models.ForeignKey(Table_Eleve, on_delete=models.CASCADE, blank=True, default=None, null=True,
                              related_name='soumissions')

    file = models.FileField(blank=False, null=False, upload_to='devoir_soumission/',default=None)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.eleve


class Resultat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    periode_1 = "periode 1"
    periode_2 = "periode 2"
    periode_3 = "periode 3"
    periode_4 = "periode 4"
    trimestre_1 = "trimestre 1"
    trimestre_2 = "trimestre 2"
    trimestre_3 = "trimestre 3"
    semestre_1 = "semestre 1"
    semestre_2 = "semestre 2"

    period_choices = [
        (periode_1, periode_1),
        (periode_2, periode_2),
        (periode_3, periode_3),
        (periode_4, periode_4),
        (trimestre_1, trimestre_1),
        (trimestre_2, trimestre_2),
        (trimestre_3, trimestre_3),
        (semestre_1, semestre_1),
        (semestre_2, semestre_2),

    ]

    periode = models.CharField(max_length=30, choices=period_choices, blank=False, null=False, default=None)

    cour = models.OneToOneField(Cour, on_delete=models.CASCADE, blank=True, null=True, related_name='cours')
    eleve = models.OneToOneField(Table_Eleve, on_delete=models.CASCADE, blank=True, null=True,
                                 related_name='resultats')
    note = models.IntegerField(blank=False, null=False, default=0)

    def __str__(self):
        return self.periode
