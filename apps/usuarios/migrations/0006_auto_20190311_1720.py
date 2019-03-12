# Generated by Django 2.0.8 on 2019-03-11 21:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_user_docente_celular'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_docente',
            name='celular',
            field=models.IntegerField(validators=[django.core.validators.RegexValidator(code='solo numeral', message='Un celular tiene 8 dígitos numerales', regex='^[0-9]{8}')]),
        ),
    ]
