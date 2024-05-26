import uuid

from django.db import models

from Institution.models import Classe


class Communication(models.Model):
    id = models.AutoField(primary_key=True, unique=True, default=uuid.uuid4)
    classe = models.ManyToManyField(Classe, null=True, blank=True)
    message = models.TextField(blank=False, null=False)
    date = models.DateTimeField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.message)
