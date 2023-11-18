from rest_framework import viewsets
from .serializer import Registro_mecSerializer
from .models import registro_mecanico

class Registro_mecViewSet(viewsets.ModelViewSet):
    queryset=registro_mecanico.objects.all()
    serializer_class=Registro_mecSerializer