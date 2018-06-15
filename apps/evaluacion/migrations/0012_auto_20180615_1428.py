# Generated by Django 2.0.5 on 2018-06-15 18:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('evaluacion', '0011_auto_20180615_0850'),
    ]

    operations = [
        migrations.CreateModel(
            name='cuestionario_aevaluacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta_1', models.PositiveIntegerField(choices=[(1, 'Nunca'), (2, 'Casi Nunca'), (3, 'A Veces'), (4, 'Casi Siempre'), (5, 'Siempre')], default=1, verbose_name='¿El docente cumple con el horario de clases establecido?')),
                ('pregunta_2', models.PositiveIntegerField(choices=[(1, 'Nunca'), (2, 'Casi Nunca'), (3, 'A Veces'), (4, 'Casi Siempre'), (5, 'Siempre')], default=1, verbose_name='¿El docente presenta el Plan de asignatura a los estudiantes al inicio de la actividad académica?')),
                ('pregunta_3', models.PositiveIntegerField(choices=[(1, 'Nunca'), (2, 'Casi Nunca'), (3, 'A Veces'), (4, 'Casi Siempre'), (5, 'Siempre')], default=1, verbose_name='¿El docente concluye los contenidos temáticos y/o actividades propuestos en el Plan de asignatura?')),
                ('pregunta_4', models.PositiveIntegerField(choices=[(1, 'Nunca'), (2, 'Casi Nunca'), (3, 'A Veces'), (4, 'Casi Siempre'), (5, 'Siempre')], default=1, verbose_name='¿El docente promueve el análisis crítico, la creatividad y el aprendizaje independiente en los estudiantes?')),
                ('pregunta_5', models.PositiveIntegerField(choices=[(1, 'Nunca'), (2, 'Casi Nunca'), (3, 'A Veces'), (4, 'Casi Siempre'), (5, 'Siempre')], default=1, verbose_name='¿El docente se relaciona con los estudiantes sin discriminación de raza, género, clase social, posición económica, credo religioso o ideología-política.?')),
                ('pregunta_6', models.PositiveIntegerField(choices=[(1, 'Nunca'), (2, 'Casi Nunca'), (3, 'A Veces'), (4, 'Casi Siempre'), (5, 'Siempre')], default=1, verbose_name='¿El docente motiva a los alumnos para la participación activa del mismo en clases?')),
                ('pregunta_7', models.PositiveIntegerField(choices=[(1, 'Nunca'), (2, 'Casi Nunca'), (3, 'A Veces'), (4, 'Casi Siempre'), (5, 'Siempre')], default=1, verbose_name='¿El docente presta atención individual o colectiva a los alumnos que solicitan consulta fuera de horarios de clases?')),
                ('pregunta_8', models.PositiveIntegerField(choices=[(1, 'Nunca'), (2, 'Casi Nunca'), (3, 'A Veces'), (4, 'Casi Siempre'), (5, 'Siempre')], default=1, verbose_name='¿El docente utiliza medios educativos de apoyo al aprendizaje, tales como Pizarra, retroproyector  u otros?')),
                ('pregunta_9', models.PositiveIntegerField(choices=[(1, 'Nunca'), (2, 'Casi Nunca'), (3, 'A Veces'), (4, 'Casi Siempre'), (5, 'Siempre')], default=1, verbose_name='¿El docente facilita texto guía, apuntes, guías de ejercicios prácticos u otros materiales preparados por él?')),
                ('pregunta_10', models.PositiveIntegerField(choices=[(1, 'Nunca'), (2, 'Casi Nunca'), (3, 'A Veces'), (4, 'Casi Siempre'), (5, 'Siempre')], default=1, verbose_name='¿El docente proporciona la Bibliografía básica contenida en el Plan de asignatura?')),
                ('pregunta_11', models.PositiveIntegerField(choices=[(1, 'Nunca'), (2, 'Casi Nunca'), (3, 'A Veces'), (4, 'Casi Siempre'), (5, 'Siempre')], default=1, verbose_name='¿El docente valora los conocimientos previos de los estudiantes, respecto a  las asignaturas precedentes?')),
                ('pregunta_12', models.PositiveIntegerField(choices=[(1, 'Nunca'), (2, 'Casi Nunca'), (3, 'A Veces'), (4, 'Casi Siempre'), (5, 'Siempre')], default=1, verbose_name='¿El docente implementa procedimientos adecuados para la evaluación del aprendizaje?')),
                ('pregunta_13', models.PositiveIntegerField(choices=[(1, 'Nunca'), (2, 'Casi Nunca'), (3, 'A Veces'), (4, 'Casi Siempre'), (5, 'Siempre')], default=1, verbose_name='¿El docente elabora las preguntas de examen en correspondencia con los temas avanzados en la asignatura?')),
                ('pregunta_14', models.PositiveIntegerField(choices=[(1, 'Nunca'), (2, 'Casi Nunca'), (3, 'A Veces'), (4, 'Casi Siempre'), (5, 'Siempre')], default=1, verbose_name='¿El docente asigna al estudiante el tiempo suficiente y necesario para la resolución del examen aplicado?')),
                ('pregunta_15', models.PositiveIntegerField(choices=[(1, 'Nunca'), (2, 'Casi Nunca'), (3, 'A Veces'), (4, 'Casi Siempre'), (5, 'Siempre')], default=1, verbose_name='¿El docente informa a los estudiantes sobre los resultados y debilidades identificadas en la evaluación, en un plazo no mayor a los 10 días?')),
                ('pregunta_16', models.PositiveIntegerField(choices=[(1, 'Nunca'), (2, 'Casi Nunca'), (3, 'A Veces'), (4, 'Casi Siempre'), (5, 'Siempre')], default=1, verbose_name='¿El docente domina los temas de la asignatura?')),
                ('pregunta_17', models.PositiveIntegerField(choices=[(1, 'Nunca'), (2, 'Casi Nunca'), (3, 'A Veces'), (4, 'Casi Siempre'), (5, 'Siempre')], default=1, verbose_name='¿El docente aclara las preguntas efectuadas por los alumnos sobre los temas avanzados?')),
                ('pregunta_18', models.PositiveIntegerField(choices=[(1, 'Nunca'), (2, 'Casi Nunca'), (3, 'A Veces'), (4, 'Casi Siempre'), (5, 'Siempre')], default=1, verbose_name='¿El docente tiene claridad expositiva en el desarrollo de los temas?')),
                ('pregunta_19', models.PositiveIntegerField(choices=[(1, 'Nunca'), (2, 'Casi Nunca'), (3, 'A Veces'), (4, 'Casi Siempre'), (5, 'Siempre')], default=1, verbose_name='¿El docente desarrolla los temas en una secuencia lógica?')),
                ('creacion', models.DateTimeField(auto_now=True)),
                ('evaluacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evaluacion.evaluacion')),
            ],
        ),
        migrations.CreateModel(
            name='token_aevaluacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_ran', models.BigIntegerField(default=6989237589)),
                ('usado', models.BooleanField(default=False)),
                ('creacion', models.DateTimeField(auto_now=True)),
                ('evaluacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evaluacion.evaluacion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='token_alumno',
            name='numero_ran',
            field=models.BigIntegerField(default=6215567506),
        ),
        migrations.AlterField(
            model_name='token_dcarrera',
            name='numero_ran',
            field=models.BigIntegerField(default=3486825024),
        ),
    ]
