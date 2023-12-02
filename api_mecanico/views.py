from .serializer import Registro_mecSerializer
from .models import Registro_mecanico 
from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework.response import Response

@api_view(['GET'])
def Lista_mecanico(request):
    registro_mecanico = Registro_mecanico.objects.all()
    serializer = Registro_mecSerializer(registro_mecanico, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def Detalle_Mecanico(request, pk):
    registro_mecanico = Registro_mecanico.objects.get(id=pk)
    serializer = Registro_mecSerializer(registro_mecanico, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def Crear_registro(request):
    serializer = Registro_mecSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)

    return Response(serializer.data)


@api_view(['PUT'])
def Actualizar_mecanico(request, pk):
    Registro_mecanico = Registro_mecanico.objects.get(id=pk)
    serializer = Registro_mecSerializer(instance=Registro_mecanico, data=request.data)

    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)


@api_view(['DELETE'])
def Eliminar_mecanico(request, pk):
    Registro_mecanico = Registro_mecanico.objects.get(id=pk)
    Registro_mecanico.delete()

    return Response('Eliminado')