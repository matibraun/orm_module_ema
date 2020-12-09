from rest_framework.serializers import ModelSerializer
from crm.models import Paciente, Area, Usuario, Provincia, Domicilio, Derivacion, Tratamiento, Diagnostico, FormaClinica, Sintomas, TerapiasRehabilitacion, Taller, Reunion, SituacionHabitacional, SituacionLaboral, CoberturaMedica, TallerPaciente

class PacienteSerializer(ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'
        
class AreaSerializer(ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'
        
class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        
class ProvinciaSerializer(ModelSerializer):
    class Meta:
        model = Provincia
        fields = '__all__'
        
class DomicilioSerializer(ModelSerializer):
    class Meta:
        model = Domicilio
        fields = '__all__'
        
class PacienteDerivacion(ModelSerializer):
    class Meta:
        model = Derivacion
        fields = '__all__'
        
class PacienteTratamiento(ModelSerializer):
    class Meta:
        model = Tratamiento
        fields = '__all__'
        
class DiagnosticoSerializer(ModelSerializer):
    class Meta:
        model = Diagnostico
        fields = '__all__'
        
class FormaClinicaSerializer(ModelSerializer):
    class Meta:
        model = FormaClinica
        fields = '__all__'
        
class SintomasSerializer(ModelSerializer):
    class Meta:
        model = Sintomas
        fields = '__all__'
        
class TerapiasRehabilitacionSerializer(ModelSerializer):
    class Meta:
        model = TerapiasRehabilitacion
        fields = '__all__'
        
class TallerSerializer(ModelSerializer):
    class Meta:
        model = Taller
        fields = '__all__'
        
class ReunionSerializer(ModelSerializer):
    class Meta:
        model = Reunion
        fields = '__all__'
        
class SituacionHabitacionalSerializer(ModelSerializer):
    class Meta:
        model = SituacionHabitacional
        fields = '__all__'
        
class SituacionLaboralSerializer(ModelSerializer):
    class Meta:
        model = SituacionLaboral
        fields = '__all__'
        
class CoberturaMedicaSerializer(ModelSerializer):
    class Meta:
        model = CoberturaMedica
        fields = '__all__'
        
class TallerPacienteSerializer(ModelSerializer):
    class Meta:
        model = TallerPaciente
        fields = '__all__'