# Generated by Django 2.0.8 on 2018-10-01 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluacion', '0034_auto_20181001_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token_aevaluacion',
            name='numero_ran',
            field=models.BigIntegerField(default=6716680329),
        ),
        migrations.AlterField(
            model_name='token_alumno',
            name='numero_ran',
            field=models.BigIntegerField(default=771997853),
        ),
        migrations.AlterField(
            model_name='token_dcarrera',
            name='numero_ran',
            field=models.BigIntegerField(default=4140426309),
        ),
    ]
