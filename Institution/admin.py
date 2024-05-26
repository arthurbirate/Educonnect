from django.contrib import admin
from .models import  Institution,Classe,Section,Promotion

# Register your models here.

admin.site.register(Institution)
admin.site.register(Classe)
admin.site.register(Section)
admin.site.register(Promotion)