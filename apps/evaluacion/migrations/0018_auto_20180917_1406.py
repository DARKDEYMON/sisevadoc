# Generated by Django 2.1.1 on 2018-09-17 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluacion', '0017_auto_20180619_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token_aevaluacion',
            name='numero_ran',
            field=models.BigIntegerField(default=2914294604),
        ),
        migrations.AlterField(
            model_name='token_alumno',
            name='numero_ran',
            field=models.BigIntegerField(default=3691670974),
        ),
        migrations.AlterField(
            model_name='token_dcarrera',
            name='numero_ran',
            field=models.BigIntegerField(default=8868959388),
        ),
    ]