# Generated by Django 2.0.8 on 2018-10-01 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluacion', '0032_auto_20181001_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token_aevaluacion',
            name='numero_ran',
            field=models.BigIntegerField(default=7650396227),
        ),
        migrations.AlterField(
            model_name='token_alumno',
            name='numero_ran',
            field=models.BigIntegerField(default=4006859091),
        ),
        migrations.AlterField(
            model_name='token_dcarrera',
            name='numero_ran',
            field=models.BigIntegerField(default=6290911663),
        ),
    ]
