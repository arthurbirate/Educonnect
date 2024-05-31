import uuid

from django.conf import settings
from django.db import models
# from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractUser, User
from django.utils.translation import gettext_lazy as _

from Institution.models import Institution, Classe


## creation des tables ##


# class User(AbstractUser):
#     is_prof = models.BooleanField(_('prof'), default=False)
#     is_parent = models.BooleanField(_('parent'), default=False)
#     is_eleve = models.BooleanField(_('eleve'), default=False)


class Table_Parent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, related_name='parent')
    name = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=50, blank=False, null=False)
    telephone = models.CharField(max_length=15, blank=False, null=False)
    email = models.EmailField(blank=True, null=True, unique=True)

    def __str__(self):
        return self.user


class Table_Eleve(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='eleve', default=None,
                                null=True)

    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, default=None, null=True,
                                    related_name='eleves')
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, default=None, null=True, blank=True)
    parent = models.ForeignKey(Table_Parent, on_delete=models.CASCADE, related_name='eleves', default=None, null=True,
                               blank=True)
    address = models.CharField(max_length=50, blank=False, null=False)
    telephone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True, unique=True)
    # document = models.ForeignKey('Document_Eleve', on_delete=models.CASCADE, default=None, null=True, related_name='eleves')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    def __str__(self):
        return self.user.first_name if self.user else "No User"


class Table_Professeur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='professeur',
                                default=None)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, default=None, null=True,
                                    related_name='professeurs')
    # document = models.ForeignKey('Document_Prof', on_delete=models.CASCADE, default=None, null=True,
    #                              related_name='professeurs')
    address = models.CharField(max_length=50, blank=False, null=False)
    telephone = models.CharField(max_length=15, blank=True, null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)

    def __str__(self):
        return self.user.first_name
