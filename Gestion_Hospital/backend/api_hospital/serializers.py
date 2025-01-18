from rest_framework import serializers
from .models import Paciente, Medico, Cita

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = '__all__'

class CitaSerializer(serializers.ModelSerializer):
    paciente = serializers.PrimaryKeyRelatedField(queryset=Paciente.objects.all())
    medico = serializers.PrimaryKeyRelatedField(queryset=Medico.objects.all())

    class Meta:
        model = Cita
        fields = '__all__'