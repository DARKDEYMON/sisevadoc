# Generated by Django 2.0.8 on 2018-10-01 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluacion', '0033_auto_20181001_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token_aevaluacion',
            name='numero_ran',
            field=models.BigIntegerField(default=6587551473),
        ),
        migrations.AlterField(
            model_name='token_alumno',
            name='numero_ran',
            field=models.BigIntegerField(default=6856770074),
        ),
        migrations.AlterField(
            model_name='token_dcarrera',
            name='numero_ran',
            field=models.BigIntegerField(default=7759333827),
        ),
    ]
