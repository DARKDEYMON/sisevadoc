# Generated by Django 2.0.8 on 2019-02-06 18:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usuarios', '0002_auto_20181115_0823'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_docente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ci', models.CharField(max_length=9, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterModelOptions(
            name='permisos',
            options={'permissions': (('usuarios', 'Permiso al modulo de usuarios'), ('academico', 'Permiso al modulo academico'), ('conf_evaluaion', 'Permiso al modulo de inilisacion de evaluacion'), ('evaluacion', 'Permiso al modulo de evaluacion'), ('dcarrera', 'Permiso al modulo de director de carrera'), ('docente', 'Permiso al modulo de Docentes'))},
        ),
    ]
