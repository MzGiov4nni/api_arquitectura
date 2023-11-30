from rest_framework import serializers
from .models import Registro_mecanico

class Registro_mecSerializer(serializers.ModelSerializer):
    class Meta:
        model=Registro_mecanico
        fields='__all__'