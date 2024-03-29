# Generated by Django 2.0.8 on 2018-10-08 14:13

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='carreras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250, validators=[django.core.validators.RegexValidator(code='dato solo alfabetico', message='El nombre solo debe contener letras y contener mínimo 4 letras', regex='^(([a-zA-ZÑÁÉÍÓÚáéíóú]{2,} )|([a-zA-ZÑÁÉÍÓÚáéíóú]{2,}))+$')])),
                ('tiempo_activo', models.DateTimeField(default=django.utils.timezone.localtime)),
            ],
        ),
        migrations.CreateModel(
            name='docentes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellidos', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(code='dato solo alfabetico', message='El apellido solo debe contener letras y contener mínimo 4 letras ', regex='^(([a-zA-ZÑÁÉÍÓÚáéíóú]{2,} )|([a-zA-ZÑÁÉÍÓÚáéíóú]{2,}))+$')])),
                ('nombre', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(code='dato solo alfabetico', message='El nombre solo debe contener letras y contener mínimo 4 letras', regex='^(([a-zA-ZÑÁÉÍÓÚáéíóú]{2,} )|([a-zA-ZÑÁÉÍÓÚáéíóú]{2,}))+$')])),
                ('carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academico.carreras')),
            ],
        ),
        migrations.CreateModel(
            name='facultad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='materias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250, validators=[django.core.validators.RegexValidator(code='dato solo alfabetico', message='El nombre solo debe contener letras y contener mínimo 4 letras', regex='^(([a-zA-ZÑÁÉÍÓÚáéíóú]{1,} )|(([a-zA-ZÑÁÉÍÓÚáéíóú]{1,})))+$')])),
                ('sigla', models.CharField(max_length=25, validators=[django.core.validators.RegexValidator(code='dato solo alfabetico', message='La sigla contiene tres letras seguidas de un guion y tres números Ej: SIS-130 en mayusculas', regex='^[A-Z]{3}-[0-9]{3}$')])),
                ('carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academico.carreras')),
            ],
        ),
        migrations.AddField(
            model_name='carreras',
            name='facultad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academico.facultad'),
        ),
    ]
