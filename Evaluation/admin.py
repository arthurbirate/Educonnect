from django.contrib import admin
from Evaluation.models import Evaluation,Cour,Devoir_Soumission,Resultat
# Register your models here.


admin.site.register(Evaluation)
admin.site.register(Resultat)
admin.site.register(Cour)
admin.site.register(Devoir_Soumission)