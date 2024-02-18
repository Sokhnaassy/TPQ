from django.urls import path
from . import views

urlpatterns = [
    path('', views.BASE , name='BASE'),
    path('contact/', views.contact_view, name='contact'),
    path('inscription/', views.inscription_view, name='inscription'),
    path('connexion/', views.connexion_view, name='connexion'),
    path('validsim/', views.validsim_view, name='validsim'),
    path('dashbord_u/', views.dashbord_u_view, name='dashbord_u'),
    path('dashbord_a/', views.dashbord_a_view, name='dashbord_a'),

]
