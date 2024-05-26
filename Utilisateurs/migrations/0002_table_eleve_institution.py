# Generated by Django 4.2.13 on 2024-05-26 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Institution', '0002_initial'),
        ('Utilisateurs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='table_eleve',
            name='institution',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='Institution.institution'),
        ),
    ]