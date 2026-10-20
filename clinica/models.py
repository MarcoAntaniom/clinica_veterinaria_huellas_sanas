from django.db import models

# Create your models here.

class Especie(models.Model):
    nombre = models.CharField(max_length=80, unique=True)
    
    def __str__(self):
        return self.nombre
    
class Raza(models.Model):
    nombre = models.CharField(max_length=80, unique=True)
    
    def __str__(self):
        return self.nombre

class Mascota(models.Model):
    nombre = models.CharField(max_length=90)
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE)
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE)
    nombre_duenio = models.CharField(max_length=70)
    
    def __str__(self):
        return f"{self.nombre} Dueño: {self.nombre_duenio}"

class EstadoCita(models.Model):
    nombre = models.CharField(max_length=60, unique=True)
    descripcion = models.CharField(max_length=120)
    
    def __str__(self):
        return self.nombre

class Citas(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    motivo_consulta = models.TextField()
    estado = models.ForeignKey(EstadoCita, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.mascota.nombre} Fecha: {self.fecha} Hora: {self.hora}"
