from django.db import models

class Registro_mecanico(models.Model):
    Nombre_Completo=models.CharField(max_length=100)
    nickname=models.CharField(max_length=50)
    Edad=models.PositiveBigIntegerField()
    especialidad = models.CharField(max_length=100)
    activo=models.BooleanField(default=True)
    estado=models.CharField(max_length=1, default='DEFAULT VALUE')

    class Meta:
        db_table = 'Registro_mecanico'

    def __str__(self) -> str:
        return self.Nombre_Completo
