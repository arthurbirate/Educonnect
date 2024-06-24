from django.urls import path

from Utilisateurs import views

urlpatterns = [

    # path('', views.index, name='index'),
    path("", views.loginUser, name='login'),
    path("dashboard/", views.dashboard, name='dashboard'),
    path("dashboard_professeur/", views.dashboard_professeur, name='dashboard_professeur'),

    path("logout/", views.logoutUser, name="logout"),
    path("creer_eleve/", views.creer_eleve, name="creer_eleve"),
    path("creer_professeur/", views.creer_professeur, name="creer_professeur")
]
