# Generated by Django 2.0.8 on 2019-01-16 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluacion', '0005_evaluacion_periodo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token_aevaluacion',
            name='creacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
