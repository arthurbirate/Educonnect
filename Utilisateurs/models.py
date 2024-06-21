import uuid

from django.conf import settings
from django.db import models
# from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractUser, User
from django.utils.translation import gettext_lazy as _


class Table_Parent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, related_name='parents')
    first_name = models.CharField(max_length=50, blank=True, null=True, default=None)
    last_name = models.CharField(max_length=50, blank=True, null=True, default=None)
    address = models.CharField(max_length=50, blank=False, null=False)
    telephone = models.CharField(max_length=15, blank=False, null=False)
    email = models.EmailField(blank=True, null=True, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Table_Eleve(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='eleve', default=None, null=True)
    first_name = models.CharField(max_length=200, null=True, blank=True, default=None)
    last_name = models.CharField(max_length=200, null=True, blank=True, default=None)
    classe = models.ForeignKey('Institution.Classe', on_delete=models.CASCADE, default=None, null=True, blank=True)

    gender_Choices = {
        ('M', 'Male'),
        ('F', 'Femelle'),
    }
    gender = models.CharField(max_length=10, choices=gender_Choices, null=True, blank=True, default=None)
    section = models.ForeignKey('Institution.Section', on_delete=models.CASCADE, default=None, null=True, blank=True)
    parent = models.ForeignKey(Table_Parent, on_delete=models.CASCADE, related_name='eleves', default=None, null=True,
                               blank=True)
    address = models.CharField(max_length=50, blank=False, null=False)
    telephone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True, unique=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Table_Professeur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='professeur',
                                default=None)
    first_name = models.CharField(max_length=200, null=True, blank=True, default=None)
    last_name = models.CharField(max_length=200, null=True, blank=True, default=None)
    gender_Choices = {
        ('M', 'Male'),
        ('F', 'Femelle'),
    }

    gender = models.CharField(max_length=10, choices=gender_Choices, null=True, blank=True)
    address = models.CharField(max_length=50, blank=False, null=False)
    telephone = models.CharField(max_length=15, blank=True, null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
