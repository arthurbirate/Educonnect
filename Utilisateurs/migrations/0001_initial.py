# Generated by Django 4.2.13 on 2024-06-21 07:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Institution', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Table_Professeur',
            fields=[
                ('first_name', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('last_name', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('gender', models.CharField(blank=True, choices=[('F', 'Femelle'), ('M', 'Male')], max_length=10, null=True)),
                ('address', models.CharField(max_length=50)),
                ('telephone', models.CharField(blank=True, max_length=15, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='professeur', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Table_Parent',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('address', models.CharField(max_length=50)),
                ('telephone', models.CharField(max_length=15)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='parents', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Table_Eleve',
            fields=[
                ('first_name', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('last_name', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('gender', models.CharField(blank=True, choices=[('F', 'Femelle'), ('M', 'Male')], default=None, max_length=10, null=True)),
                ('address', models.CharField(max_length=50)),
                ('telephone', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('classe', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Institution.classe')),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eleves', to='Utilisateurs.table_parent')),
                ('section', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Institution.section')),
                ('user', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eleve', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
