# from Django
from django.contrib.auth.models import User
from django.contrib import admin

# models
from .models import EmployeeProfile

@admin.register(EmployeeProfile)
class ProfileAdmin(admin.ModelAdmin):
    """ Configuración de la vista de listado: """

    # Campos a visializar en la tabla:
    list_display        = ('user','position')
    # Campos que actuaran como link hacia el detail:
    list_display_links  = ('user',)
    # Lista de campos considerados en la busqueda:
    search_fields       = ('user','position')
    # Lista de campos para los filtros:
    list_filter         = ('created','modified','user__is_active','user__is_superuser')

    """ Configuración de la vista de detail: """

    #
