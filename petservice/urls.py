from django.urls import path
from petservice.views import *


urlpatterns = [
    path('inicio/', inicio, name='inicio'),
    path('propietarios/', mostrar_propietarios, name='propietarios'),
    path('mascotas/', mostrar_mascotas, name='mascotas'),
    path('servicios/', mostrar_servicios, name='servicios'),
    path('veterinarios/', mostrar_veterinario, name='veterinarios'),
]

propietario = [
    path('form-propietario/', form_propietario, name='formulario_propietario'),
    path('form-mascota/', form_mascota, name='formulario_mascota'),
    path('form-veterinario/', form_veterinario, name='formulario_veterinario'),
]    

urlpatterns += propietario

busqueda = [
    path('buscar-mascota/', buscar_mascota, name='buscar_mascota'),
    path('buscar/', buscar),
]

urlpatterns += busqueda