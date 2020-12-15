"""ema_crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views.pacientes import PacientesView, PacienteView
from .views.provincias import ProvinciasView, ProvinciaView
from .views.areas import AreasView, AreaView
from .views.tratamientos import TratamientosView, TratamientoView
from .views.diagnosticos import DiagnosticosView, DiagnosticoView
from .views.usuarios import UsuariosView, UsuarioView
from .views.domicilios import DomiciliosView, DomicilioView
# from .views.derivaciones import DerivacionesView, DerivacionView
from .views.sintomas import SintomasView, SintomaView
from .views.terapiaRehabilitacion import TerapiasRehabilitacionesView, TerapiaRehabilitacionView
from .views.talleres import TalleresView, TallerView
from .views.reuniones import ReunionesView, ReunionView
from .views.formasClinicas import FormasClinicasView, FormaClinicaView
from .views.situacionesHabitacionales import SituacionesHabitacionalesView, SituacionHabitacionalView
from .views.situacionesLaborales import SituacionesLaboralesView, SituacionLaboralView
from .views.coberturasMedicas import CoberturasMedicasView, CoberturaMedicaView
from .views.composicionesFamiliares import ComposicionesFamiliaresView, ComposicionFamiliarView





urlpatterns = [
    path('pacientes/', PacientesView.as_view(), name='pacientes'),
    path('pacientes/<int:pk>', PacienteView.as_view(), name='paciente'),
    path('provincias/', ProvinciasView.as_view(), name='provincias'),
    path('provincias/<int:pk>', ProvinciaView.as_view(), name='provincia'),
    path('areas/', AreasView.as_view(), name='areas'),
    path('areas/<int:pk>', AreaView.as_view(), name='area'),
    path('tratamientos/', TratamientosView.as_view(), name='tratamientos'),
    path('tratamientos/<int:pk>', TratamientoView.as_view(), name='tratamiento'),
    path('diagnosticos/', DiagnosticosView.as_view(), name='diagnosticos'),
    path('diagnosticos/<int:pk>', DiagnosticoView.as_view(), name='diagnostico'),
    path('usuarios/', UsuariosView.as_view(), name='usuarios'),
    path('usuarios/<int:pk>', UsuarioView.as_view(), name='usuario'),
    path('domicilios/', DomiciliosView.as_view(), name='domicilios'),
    path('domicilios/<int:pk>', DomicilioView.as_view(), name='domicilio'),
    # path('derivaciones/', DerivacionesView.as_view(), name='derivaciones'),
    # path('derivacions/<int:pk>', DerivacionView.as_view(), name='derivacion'),
    path('sintomas/', SintomasView.as_view(), name='sintomas'),
    path('sintomas/<int:pk>', SintomaView.as_view(), name='sintoma'),
    path('terapias_y_rehabilitaciones/', TerapiasRehabilitacionesView.as_view(), name='terapias_y_rehabilitaciones'),
    path('terapias_y_rehabilitaciones/<int:pk>', TerapiaRehabilitacionView.as_view(), name='terapia_y_rehabilitacion'),    
    path('talleres/', TalleresView.as_view(), name='talleres'),
    path('talleres/<int:pk>', TallerView.as_view(), name='taller'),
    path('reuniones/', ReunionesView.as_view(), name='reuniones'),
    path('reuniones/<int:pk>', ReunionView.as_view(), name='reunion'),
    path('situaciones_habitacionales/', SituacionesHabitacionalesView.as_view(), name='situaciones_habitacionales'),
    path('situaciones_habitacionales/<int:pk>', SituacionHabitacionalView.as_view(), name='situacion_habitacional'),
    path('formas_clinicas/', FormasClinicasView.as_view(), name='formas_clinicas'),
    path('formas_clinicas/<int:pk>', FormaClinicaView.as_view(), name='forma_clinica'),
    path('situaciones_laborales/', SituacionesLaboralesView.as_view(), name='situaciones_laborales'),
    path('situaciones_laborales/<int:pk>', SituacionLaboralView.as_view(), name='situacion_laboral'),
    path('coberturas_medicas/', CoberturasMedicasView.as_view(), name='coberturas_medicas'),
    path('coberturas_medicas/<int:pk>', CoberturaMedicaView.as_view(), name='cobertura_medica'),
    path('composiciones_familiares/', ComposicionesFamiliaresView.as_view(), name='composiciones_familiares'),
    path('composiciones_familiares/<int:pk>', ComposicionFamiliarView.as_view(), name='composicion_familiar'),
    ]