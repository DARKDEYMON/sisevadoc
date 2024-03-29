# Generated by Django 2.0.8 on 2018-10-25 19:23

import apps.evaluacion.setting_dinamic
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0001_initial'),
        ('evaluacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluacion',
            name='gestion',
            field=models.PositiveIntegerField(default=apps.evaluacion.setting_dinamic.initial_default_gestion, validators=[django.core.validators.RegexValidator(code='dato solo numerico', message='El año solo contiene cuatro digitos numericos', regex='^[0-9]{4}$')]),
        ),
        migrations.AlterUniqueTogether(
            name='evaluacion',
            unique_together={('docente', 'gestion'), ('docente', 'gestion', 'materia')},
        ),
    ]
