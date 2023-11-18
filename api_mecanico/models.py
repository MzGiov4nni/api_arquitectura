from django.db import models

class registro_mecanico(models.Model):
    Nombre_Completo=models.CharField(max_length=100)
    nickname=models.CharField(max_length=50)
    Edad=models.PositiveBigIntegerField()
    especialidad = models.CharField(max_length=100)
    activo=models.BooleanField(default=True)
    
