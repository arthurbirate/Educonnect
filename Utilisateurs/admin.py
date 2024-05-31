from django.contrib import admin
from  .models import Table_Eleve, Table_Parent,Table_Professeur
#

# # admin.site.register(Staff)
# admin.site.register(User)
admin.site.register(Table_Professeur)
admin.site.register(Table_Eleve)
admin.site.register(Table_Parent)

# admin.site.register(Document)