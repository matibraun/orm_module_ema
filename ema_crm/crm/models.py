from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class AreaModel(models.Model):
    nombre = models.CharField(max_length=300, blank=False, null=False)


class EstadoCivilModel(models.Model):
    nombre = models.CharField(max_length=300, blank=False, null=False)


class GeneroModel(models.Model):
    nombre = models.CharField(max_length=300, blank=False, null=False)


class CoberturaMedicaModel(models.Model):
    nombre = models.CharField(max_length=300, blank=False, null=False)


class SituacionHabitacionalModel(models.Model):
    nombre = models.CharField(max_length=300, blank=False, null=False)


class SituacionLaboralModel(models.Model):
    nombre = models.CharField(max_length=300, blank=False, null=False)


class TeEnterastePorModel(models.Model):
    nombre = models.CharField(max_length=300, blank=False, null=False)


class ProvinciaModel(models.Model):
    nombre = models.CharField(max_length=300, blank=False, null=False)


class DiagnosticoModel(models.Model):
    nombre = models.CharField(max_length=300, blank=False, null=False)


class FormaClinicaModel(models.Model):
    nombre = models.CharField(max_length=300, blank=False, null=False)


class SintomaModel(models.Model):
    nombre = models.CharField(max_length=300, blank=False, null=False)


class TerapiaRehabilitacionModel(models.Model):
    nombre = models.CharField(max_length=300, blank=False, null=False)


class UserExtendidoModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dni = models.CharField(max_length=300, blank=False, null=False)
    fechaNacimiento = models.DateField(blank=False, null=False)
    telFijo = models.CharField(max_length=300, blank=True, null=True)
    telMovil = models.CharField(max_length=300, blank=False, null=False)
    area = models.ForeignKey(AreaModel, on_delete=models.RESTRICT)


class DomicilioUserModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    calle = models.CharField(max_length=300, blank=False, null=False)
    numero = models.CharField(max_length=300, blank=False, null=False)
    piso = models.CharField(max_length=300, blank=True, null=True)
    provincia = models.ForeignKey(ProvinciaModel, on_delete=models.RESTRICT)
    localidad = models.CharField(max_length=300, blank=False, null=False)
    codigoPostal = models.CharField(max_length=300, blank=False, null=False)


class PacienteModel(models.Model):
    dni = models.CharField(max_length=300, unique=True,
                           blank=False, null=False)
    nombre = models.CharField(max_length=300, blank=False, null=False)
    apellido = models.CharField(max_length=300, blank=False, null=False)
    fechaNacimiento = models.DateField(blank=False, null=False)
    nacionalidad = models.CharField(max_length=300, blank=False, null=False)
    lugarNacimiento = models.CharField(max_length=300, blank=False, null=True)
    email = models.EmailField(unique=True, blank=False, null=False)
    telFijo = models.CharField(max_length=300, blank=True, null=True)
    telMovil = models.CharField(max_length=300, blank=False, null=True)
    telAlternativo = models.CharField(max_length=300, blank=True, null=True)
    genero = models.ForeignKey(GeneroModel, on_delete=models.RESTRICT)
    estadoCivil = models.ForeignKey(
        EstadoCivilModel, on_delete=models.RESTRICT)
    fechaAlta = models.DateField(auto_now=True)
    usuarioQueRealizoAlta = models.ForeignKey(User, on_delete=models.RESTRICT)
    esSocio = models.BooleanField(default=False, blank=False, null=False)
    fechaAsociacion = models.DateField(blank=True, null=True)
    fechaUltimaCuotaPaga = models.DateField(blank=True, null=True)
    recibeMailing = models.BooleanField(default=False, blank=False, null=False)
    coberturaMedica = models.ForeignKey(
        CoberturaMedicaModel, on_delete=models.RESTRICT)
    numeroAfiliado = models.CharField(max_length=300, blank=False, null=True)
    lugarDeAtencion = models.CharField(max_length=300, blank=False, null=False)
    neurologoCabecera = models.CharField(
        max_length=300, blank=False, null=False)
    situacionHabitacional = models.ForeignKey(
        SituacionHabitacionalModel, on_delete=models.RESTRICT)
    situacionLaboral = models.ForeignKey(
        SituacionLaboralModel, on_delete=models.RESTRICT)
    fechaDiagnostico = models.DateField(blank=False, null=False)
    actividadFisica = models.BooleanField(
        default=False, blank=False, null=False)
    fumadorTabaco = models.BooleanField(default=False, blank=False, null=False)
    antecedentesEnfermedades = models.CharField(
        max_length=300, blank=True, null=True)
    tieneCUD = models.BooleanField(default=False, blank=False, null=False)
    fechaVencimientoCUD = models.DateField(blank=True, null=True)
    teEnterasteDeEmaPor = models.ForeignKey(
        TeEnterastePorModel, on_delete=models.RESTRICT)
    talleres = models.ManyToManyField(
        'TallerModel', through='TallerPacienteModel')
    gruposDeApoyo = models.ManyToManyField(
        'GrupoDeApoyoModel', through='GrupoDeApoyoPacienteModel')


class DomicilioPacienteModel(models.Model):
    paciente = models.ForeignKey(PacienteModel, on_delete=models.CASCADE)
    calle = models.CharField(max_length=300, blank=False, null=False)
    numero = models.CharField(max_length=300, blank=False, null=False)
    piso = models.CharField(max_length=300, blank=True, null=True)
    provincia = models.ForeignKey(ProvinciaModel, on_delete=models.RESTRICT)
    localidad = models.CharField(max_length=300, blank=False, null=False)
    codigoPostal = models.CharField(max_length=300, blank=False, null=False)


class DomicilioAlternativoPacienteModel(models.Model):
    paciente = models.ForeignKey(PacienteModel, on_delete=models.CASCADE)
    calle = models.CharField(max_length=300, blank=False, null=False)
    numero = models.CharField(max_length=300, blank=False, null=False)
    piso = models.CharField(max_length=300, blank=True, null=True)
    provincia = models.ForeignKey(ProvinciaModel, on_delete=models.RESTRICT)
    localidad = models.CharField(max_length=300, blank=False, null=False)
    codigoPostal = models.CharField(max_length=300, blank=False, null=False)


class ComposicionFamiliarModel(models.Model):
    paciente = models.ForeignKey(PacienteModel, on_delete=models.CASCADE)
    vinculo = models.CharField(max_length=300, blank=False, null=False)
    nombre = models.CharField(max_length=300, blank=False, null=False)
    apellido = models.CharField(max_length=300, blank=False, null=False)
    fechaNacimiento = models.DateField(blank=False, null=False)
    email = models.EmailField(unique=False, blank=False, null=False)
    telFijo = models.CharField(max_length=300, blank=True, null=True)
    telMovil = models.CharField(max_length=300, blank=False, null=False)
    ocupacion = models.CharField(max_length=300, blank=False, null=False)
    esConviviente = models.BooleanField(default=False, blank=False, null=False)


class CuotaPagaModel(models.Model):
    paciente = models.ForeignKey(PacienteModel, on_delete=models.CASCADE)
    correspondienteAlAno = models.CharField(
        max_length=300, blank=False, null=False)
    montoPagado = models.CharField(max_length=300, blank=False, null=False)
    fechaPago = models.DateField(auto_now=True)
    usuarioQueCargoPago = models.ForeignKey(User, on_delete=models.RESTRICT)


class TratamientoModel(models.Model):
    paciente = models.ForeignKey(PacienteModel, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now=True)
    medicoTratante = models.CharField(max_length=300, blank=False, null=False)
    tratamiento = models.CharField(max_length=300, blank=False, null=False)
    droga = models.CharField(max_length=300, blank=False, null=False)
    marca = models.CharField(max_length=300, blank=False, null=False)
    usuarioQueCargoTratamiento = models.ForeignKey(
        User, on_delete=models.RESTRICT)


class TallerModel(models.Model):
    nombre = models.CharField(max_length=300, blank=False, null=False)
    pacientes = models.ManyToManyField(
        'PacienteModel', through='TallerPacienteModel')


class TallerPacienteModel(models.Model):
    paciente = models.ForeignKey(PacienteModel, on_delete=models.CASCADE)
    taller = models.ForeignKey(TallerModel, on_delete=models.CASCADE)


class GrupoDeApoyoModel(models.Model):
    nombre = models.CharField(max_length=300, blank=False, null=False)
    pacientes = models.ManyToManyField(
        'PacienteModel', through='GrupoDeApoyoPacienteModel')


class GrupoDeApoyoPacienteModel(models.Model):
    paciente = models.ForeignKey(PacienteModel, on_delete=models.CASCADE)
    grupoDeApoyo = models.ForeignKey(
        GrupoDeApoyoModel, on_delete=models.CASCADE)


class ReunionModel(models.Model):
    paciente = models.ForeignKey(PacienteModel, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.RESTRICT)
    fecha = models.DateField(auto_now=True)
    contenido = models.TextField(blank=False, null=False)
    areaAlQueSeDerivo = models.ForeignKey(
        AreaModel, on_delete=models.RESTRICT, blank=True, null=True)
