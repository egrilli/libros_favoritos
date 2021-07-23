from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('registro', views.registro),
    path('logearse',views.logearse),
    path('panel',views.panel),
    path('logout',views.logout),
    path('colaborador',views.colaborador),
    path('administrador',views.administrador),
    path('nuevo-libro',views.nuevoLibro),
    path('book/<int:id>',views.libro),
    path('<int:id>/megusta', views.meGusta),
    path('<int:id>/nomegusta', views.noMeGusta),
    path('<int:id>/actualizar', views.actualizar),
    path('<int:id>/borrar', views.borrar),
    


]
