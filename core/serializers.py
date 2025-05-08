from rest_framework import serializers
from .models import Paciente
from .models import Cita
from .models import Atencion
from .models import Medicamento
from .models import ServicioMedico
from django.contrib.auth.models import User


class ServicioMedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicioMedico
        fields = '__all__'


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

class CitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cita
        fields = '__all__'

class AtencionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atencion
        fields = '__all__'

class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = '__all__'

class MedicoRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user
