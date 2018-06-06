# Generated by Django 2.0.5 on 2018-06-05 21:38

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='materias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25, validators=[django.core.validators.RegexValidator(code='dato solo alfabetico', message='El nombre solo debe contener letras y contener mínimo 4 letras', regex='[a-zA-ZñÑáéíóúÁÉÍÓÚ ]{4,25}')])),
                ('sigla', models.CharField(max_length=25, validators=[django.core.validators.RegexValidator(code='dato solo alfabetico', message='La sigla contiene tres letras seguidas de un guion y tres números Ej: SIS-130', regex='[A-Z]{3}-[0-9]{3}')])),
            ],
        ),
        migrations.AlterField(
            model_name='carreras',
            name='nombre',
            field=models.CharField(max_length=25, validators=[django.core.validators.RegexValidator(code='dato solo alfabetico', message='El nombre solo debe contener letras y contener mínimo 4 letras en mayusculas', regex='^[A-ZÑÁÉÍÓÚ ]{4,25}$')]),
        ),
        migrations.AddField(
            model_name='materias',
            name='carrera',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academico.carreras'),
        ),
    ]