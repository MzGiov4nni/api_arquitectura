# Generated by Django 4.2.6 on 2023-11-18 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_mecanico', '0002_registro_mecanico_delete_programmer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registro_mecanico',
            old_name='age',
            new_name='Edad',
        ),
        migrations.RenameField(
            model_name='registro_mecanico',
            old_name='fullname',
            new_name='Nombre_Completo',
        ),
    ]
