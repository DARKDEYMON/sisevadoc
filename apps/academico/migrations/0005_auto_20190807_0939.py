# Generated by Django 2.0.8 on 2019-08-07 13:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0004_auto_20190207_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materias',
            name='nombre',
            field=models.CharField(max_length=250, validators=[django.core.validators.RegexValidator(code='dato solo alfabetico', message='El nombre solo debe contener letras y contener mínimo 4 letras', regex='^(([a-zA-ZÑÁÉÍÓÚáéíóúñ]{1,} )|(([a-zA-ZÑÁÉÍÓÚáéíóúñ]{1,})))+$')]),
        ),
    ]