from django.db import models

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=8, unique=True)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=15)
    direccion = models.TextField(blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.dni})"

class Cita(models.Model):
    ESTADO_CHOICES = [
        ('PENDIENTE', 'Pendiente'),
        ('ATENDIDA', 'Atendida'),
        ('CANCELADA', 'Cancelada'),
    ]

    paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE, related_name='citas')
    fecha_cita = models.DateTimeField()
    motivo = models.CharField(max_length=255)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='PENDIENTE')

    def __str__(self):
        return f'Cita con {self.paciente.nombre} el {self.fecha_cita.strftime("%Y-%m-%d %H:%M")}'


class Atencion(models.Model):
    cita = models.OneToOneField('Cita', on_delete=models.CASCADE, related_name='atencion')
    diagnostico = models.TextField()
    recomendaciones = models.TextField()
    fecha_atencion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Atención - {self.cita.paciente.nombre} ({self.cita.fecha_cita.date()})"


class Medicamento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    presentacion = models.CharField(max_length=100)  # ej: "Tableta 500mg"
    laboratorio = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nombre

class ServicioMedico(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)  # ej: Ecografía, Análisis, Rayos X
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"

