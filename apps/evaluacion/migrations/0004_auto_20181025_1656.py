# Generated by Django 2.0.8 on 2018-10-25 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluacion', '0003_evaluacion_token_generate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuestionario_aevaluacion',
            name='creacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='cuestionario_alumno',
            name='creacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='cuestionario_dcarrera',
            name='creacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='evaluacion',
            name='creacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='token_alumno',
            name='creacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='token_dcarrera',
            name='creacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]