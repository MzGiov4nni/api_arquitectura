# Generated by Django 4.2.6 on 2023-11-30 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_mecanico', '0003_rename_age_registro_mecanico_edad_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro_mecanico',
            name='estado',
            field=models.CharField(default='DEFAULT VALUE', max_length=1),
        ),
        migrations.AlterModelTable(
            name='registro_mecanico',
            table='registro_mecanico',
        ),
    ]
