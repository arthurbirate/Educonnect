import uuid

from django.contrib.auth.models import User
from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

# from Evaluation.models import Cour


# Create your models here.


class Institution(TenantMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    promotion = models.ManyToManyField('Promotion', blank=True, null=True, default=None, related_name='institutions')
    contact_number = models.CharField(max_length=200, unique=True, null=False, blank=False)
    address = models.CharField(max_length=200, unique=True, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Domain(DomainMixin):
    pass


class Promotion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Section(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    promotion = models.ForeignKey(Promotion, related_name="sections", on_delete=models.CASCADE, null=False, blank=False,
                                  default=None)
    # cours = models.ManyToManyField("Evaluation.Cour", blank=True, null=True, default=None, related_name='sections')
    name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Classe(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    promotion = models.ForeignKey(Promotion, related_name="classes", on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
