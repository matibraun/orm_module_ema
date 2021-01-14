from rest_framework.serializers import ModelSerializer
from crm.models import PacienteModel, AreaModel, UserExtendidoModel, ProvinciaModel, DomicilioPacienteModel, TratamientoModel, DiagnosticoModel, FormaClinicaModel, SintomaModel, TerapiaRehabilitacionModel, TallerModel, ReunionModel, SituacionHabitacionalModel, SituacionLaboralModel, CoberturaMedicaModel, ComposicionFamiliarModel, TallerPacienteModel, EstadoCivilModel, GeneroModel, DomicilioAlternativoPacienteModel, CuotaPagaModel
from django.contrib.auth.models import User


class PacienteSerializer(ModelSerializer):
    class Meta:
        model = PacienteModel
        fields = '__all__'


class AreaSerializer(ModelSerializer):
    class Meta:
        model = AreaModel
        fields = '__all__'


class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = UserExtendidoModel
        exclude = ('user',)


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProvinciaSerializer(ModelSerializer):
    class Meta:
        model = ProvinciaModel
        fields = '__all__'


class EstadoCivilSerializer(ModelSerializer):
    class Meta:
        model = EstadoCivilModel
        fields = '__all__'


class GeneroSerializer(ModelSerializer):
    class Meta:
        model = GeneroModel
        fields = '__all__'


class DomicilioSerializer(ModelSerializer):
    class Meta:
        model = DomicilioPacienteModel
        fields = '__all__'


class DomicilioAlternativoSerializer(ModelSerializer):
    class Meta:
        model = DomicilioAlternativoPacienteModel
        fields = '__all__'


# class DerivacionSerializer(ModelSerializer):
#     class Meta:
#         model = DerivacionModel
#         fields = '__all__'


class TratamientoSerializer(ModelSerializer):
    class Meta:
        model = TratamientoModel
        fields = '__all__'


class DiagnosticoSerializer(ModelSerializer):
    class Meta:
        model = DiagnosticoModel
        fields = '__all__'


class FormaClinicaSerializer(ModelSerializer):
    class Meta:
        model = FormaClinicaModel
        fields = '__all__'


class SintomaSerializer(ModelSerializer):
    class Meta:
        model = SintomaModel
        fields = '__all__'


class TerapiaRehabilitacionSerializer(ModelSerializer):
    class Meta:
        model = TerapiaRehabilitacionModel
        fields = '__all__'


class TallerSerializer(ModelSerializer):
    class Meta:
        model = TallerModel
        fields = '__all__'


class ReunionSerializer(ModelSerializer):
    class Meta:
        model = ReunionModel
        fields = '__all__'


class SituacionHabitacionalSerializer(ModelSerializer):
    class Meta:
        model = SituacionHabitacionalModel
        fields = '__all__'


class SituacionLaboralSerializer(ModelSerializer):
    class Meta:
        model = SituacionLaboralModel
        fields = '__all__'


class CoberturaMedicaSerializer(ModelSerializer):
    class Meta:
        model = CoberturaMedicaModel
        fields = '__all__'


class TallerPacienteSerializer(ModelSerializer):
    class Meta:
        model = TallerPacienteModel
        fields = '__all__'


class ComposicionFamiliarSerializer(ModelSerializer):
    class Meta:
        model = ComposicionFamiliarModel
        fields = '__all__'


class CuotaPagaSerializer(ModelSerializer):
    class Meta:
        model = CuotaPagaModel
        fields = '__all__'
