# Generated by Django 2.0.5 on 2018-06-14 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluacion', '0008_auto_20180613_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluacion',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='token_alumno',
            name='numero_ran',
            field=models.PositiveIntegerField(default=6894395649),
        ),
    ]
