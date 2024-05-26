import uuid

# from django.contrib.auth.models import User
from django.db import models
# from Utilisateurs.models import User


# Create your models here.


class Institution(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    user = models.OneToOneField('Utilisateurs.User', on_delete=models.CASCADE,default=None,null=True, blank=True)
    promotion = models.ManyToManyField('Promotion', related_name="institutions", blank=True, null=True)
    section = models.ManyToManyField('Section', related_name="institutions", blank=True, null=True)
    contact_number = models.CharField(max_length=200, unique=True, null=False, blank=False)
    address = models.CharField(max_length=200, unique=True, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Promotion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Section(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    promotion = models.ForeignKey(Promotion, related_name="sections", on_delete=models.CASCADE, null=True, blank=True)
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
