from django.shortcuts import render
from datetime import date
from django.utils.dateparse import parse_date
from .models import *

# Create your views here.

def inicio(request):
    hoy = date.today()
    
    citas_hoy = (
        Citas.objects.filter(fecha=hoy).select_related("mascota", "mascota_especie", "estado").order_by("hora")
    )
    
    contexto = {
        "total_hoy": citas_hoy.count(),
        "pendientes": Citas.objects.filter(
            estado__nombre="Pendiente"
        ).count(),
        "atendidas": Citas.objects.filter(
            estado__nombre="Atendida"
        ).count(),
        "total_mascotas": Mascota.objects.count(),
        "citas_hoy": citas_hoy,
    }

    return render(request, 'dashboard.html', context=contexto)

def listar_citas(request):
    citas = Citas.objects.select_related(
        "mascota",
        "mascota__especie",
        "mascota__raza",
        "estado",
    )

    fecha_filtro = request.GET.get("fecha", "").strip()
    estado_filtro = request.GET.get("estado", "").strip()

    if fecha_filtro:
        fecha = parse_date(fecha_filtro)
        if fecha:
            citas = citas.filter(fecha=fecha)

    if estado_filtro:
        citas = citas.filter(estado__nombre=estado_filtro)

    contexto = {
        "citas": citas.order_by("fecha", "hora"),
        "estados": EstadoCita.objects.all().order_by("nombre"),
        "fecha_filtro": fecha_filtro,
        "estado_filtro": estado_filtro,
    }

    return render(request, "veterinaria/citas_list.html", contexto)
