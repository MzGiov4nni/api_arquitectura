from rest_framework import serializers
from .models import registro_mecanico

class Registro_mecSerializer(serializers.ModelSerializer):
    class Meta:
        model=registro_mecanico
        fields='__all__'