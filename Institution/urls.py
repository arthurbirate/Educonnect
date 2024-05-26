from django.urls import path

from . import views

urlpatterns = [

    path("creer_institution/", views.createInstitution, name="cree_Institution"),

]
