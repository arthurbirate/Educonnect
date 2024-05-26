from django.contrib import admin
from  .models import  User,Table_Eleve, Table_Parent,Table_Professeur
#
#
admin.site.register(User)
# # admin.site.register(Staff)
# # admin.site.register(Role)
admin.site.register(Table_Professeur)
admin.site.register(Table_Eleve)
admin.site.register(Table_Parent)

# admin.site.register(Document)