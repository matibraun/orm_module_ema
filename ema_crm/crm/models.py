from django.db import models

# Create your models here.

class Paciente(models.Model):
        
    dni = models.CharField(max_length=300, unique=True, blank=False, null=False)
    nombre = models.CharField(max_length=300, blank=False, null=False)
    apellido = models.CharField(max_length=300, blank=False, null=False)
    fechaNacimiento = models.DateField(blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    telFijo = models.CharField(max_length=300, blank=True, null=True)
    telMovil = models.CharField(max_length=300, blank=False, null=False)
    # domicilios = 
    fechaAlta = models.DateField(auto_now=True)
    usuarioQueRealizoAlta_id = models.IntegerField(blank=False, null=False)
    areaALaQueSeDerivo_id = models.IntegerField(blank=False, null=False)
    esSocio = models.BooleanField(default=False, blank=False, null=False)
    fechaAsociacion = models.DateField(blank=True, null=True)
    fechaUltimaCuotaPaga = models.DateField(blank=True, null=True)
    recibeMailing = models.BooleanField(default=False, blank=False, null=False)
    coberturaMedica = models.IntegerField(blank=False, null=False)
    lugarDeAtencion = models.CharField(max_length=300, blank=False, null=False)
    neurologoCabecera = models.CharField(max_length=300, blank=False, null=False)
    participaGrupoApoyoPacientes = models.BooleanField(default=False, blank=False, null=False)
    participaGrupoApoyoFamiliares = models.BooleanField(default=False, blank=False, null=False)
    fechaDiagnostico = models.DateField(blank=False, null=False)
    actividadFisica = models.BooleanField(default=False, blank=False, null=False)
    fumadorTabaco = models.BooleanField(default=False, blank=False, null=False)
    antecedentesEnfermedades = models.CharField(max_length=300, blank=True, null=True)
    tieneCUD = models.BooleanField(default=False, blank=False, null=False)
    fechaVencimientoCUD = models.DateField(blank=True, null=True)
    # derivaciones = 
    # talleres = 
    # tratamientos =
    # diagnosticos =
    # formasClinicas =
    # sintomas = 

class Area(models.Model):
    nombre = models.CharField(max_length=300, blank=False, null=False)

class Usuario(models.Model):
    dni = models.CharField(max_length=300, blank=False, null=False)
    nombre = models.CharField(max_length=300, blank=False, null=False)
    apellido = models.CharField(max_length=300, blank=False, null=False)
    fechaNacimiento = models.DateField(blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    telFijo = models.CharField(max_length=300, blank=True, null=True)
    telMovil = models.CharField(max_length=300, blank=False, null=False)
    area = models.ForeignKey(Area, on_delete=models.RESTRICT)

class Provincia(models.Model):
    nombre = models.CharField(max_length=300, blank=False, null=False)

class Domicilio(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    calle = models.CharField(max_length=300, blank=False, null=False)
    numero = models.CharField(max_length=300, blank=False, null=False)
    piso = models.CharField(max_length=300, blank=True, null=True)
    provincia = models.ForeignKey(Provincia, on_delete=models.RESTRICT)
    localidad = models.CharField(max_length=300, blank=False, null=False)
    codigoPostal = models.CharField(max_length=300, blank=False, null=False)

class Derivacion(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.RESTRICT)
    areaAlQueSeDerivo = models.ForeignKey(Area, on_delete=models.RESTRICT)

class Tratamiento(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now=True)
    medicoTratante = models.CharField(max_length=300, blank=False, null=False)
    tratamiento = models.CharField(max_length=300, blank=False, null=False)
    droga = models.CharField(max_length=300, blank=False, null=False)
    marca = models.CharField(max_length=300, blank=False, null=False)

class Diagnostico(models.Model):
    nombre = models.CharField(max_length=300, blank=False, null=False)

class FormaClinica(models.Model):
    nombre = models.CharField(max_length=300, blank=False, null=False)

class Sintomas(models.Model):
    nombre = models.CharField(max_length=300, blank=False, null=False)

class TerapiasRehabilitacion(models.Model):
    nombre = models.CharField(max_length=300, blank=False, null=False)

class Taller(models.Model):
    nombre = models.CharField(max_length=300, blank=False, null=False)

class Reunion(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.RESTRICT)
    fecha = models.DateField(auto_now=True)
    contenido = models.TextField(blank=False, null=False)

class SituacionHabitacional(models.Model):
    nombre = models.CharField(max_length=300, blank=False, null=False)

class SituacionLaboral(models.Model):
    nombre = models.CharField(max_length=300, blank=False, null=False)

class CoberturaMedica(models.Model):
    nombre = models.CharField(max_length=300, blank=False, null=False)

class TallerPaciente(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    taller = models.ForeignKey(Taller, on_delete=models.RESTRICT)

