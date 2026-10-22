from django.contrib import admin
from .models import *

# Register your models here.

class EspecieAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")

class RazaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")

class MascotaAdmin(admin.ModelAdmin):
    search_fields = ["nombre"]
    list_display = ("id", "nombre", "especie", "raza", "nombre_duenio")

class EstadoCitaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "descripcion")

class CitasAdmin(admin.ModelAdmin):
    list_filter = ["fecha"]
    list_display = ("id", "mascota", "fecha", "hora", "motivo_consulta", "estado")


admin.site.register(Especie, EspecieAdmin)
admin.site.register(Raza, RazaAdmin)
admin.site.register(Mascota, MascotaAdmin)
admin.site.register(EstadoCita, EstadoCitaAdmin)
admin.site.register(Citas, CitasAdmin)