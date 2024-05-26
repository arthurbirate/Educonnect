import uuid

from django.db import models
# from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from Institution.models import Institution, Classe


#
#
# # Create your models here.
#
#
class User(AbstractUser):
    is_eleve = models.BooleanField(_('eleve'), default=False, blank=True)
    is_parent = models.BooleanField(_('parent'), default=False, blank=True)
    is_professeur = models.BooleanField(_('professeur'), default=False, blank=True)


class Table_Parent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=50, blank=False, null=False)
    telephone = models.CharField(max_length=15, blank=False, null=False)
    email = models.EmailField(blank=True, null=True, unique=True)

    def __str__(self):
        return self.user

#
# #
# #
# # #
class Table_Eleve(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='eleves', default=None, null=True)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, default=None, null=True,
                                    related_name='users')
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, default=None, null=True)
    parent = models.ForeignKey(Table_Parent, on_delete=models.CASCADE, related_name='eleves', default=None)
    address = models.CharField(max_length=50, blank=False, null=False)
    telephone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True, unique=True)
    # document = models.ForeignKey('Document_Eleve', on_delete=models.CASCADE, default=None, null=True, related_name='eleves')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    def __str__(self):
        return self.user.first_name


class Table_Professeur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='professeurs')
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, default=None, null=True,
                                    related_name='professeurs')
    # document = models.ForeignKey('Document_Prof', on_delete=models.CASCADE, default=None, null=True,
    #                              related_name='professeurs')
    address = models.CharField(max_length=50, blank=False, null=False)
    telephone = models.CharField(max_length=15, blank=True, null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)

    def __str__(self):
        return self


# class Document_Eleve(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
#     type = models.CharField(max_length=50, blank=False, null=False)
#     File = models.FileField(upload_to='documents/', null=False, blank=False, default=None)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.type
#
#
# class Document_Prof(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
#     document_choices = [
#
#     ]
#     type = models.CharField(max_length=50, blank=False, null=False)
#     File = models.FileField(upload_to='document_prof/', null=False, blank=False, default=None)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.type
