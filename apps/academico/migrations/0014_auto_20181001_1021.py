# Generated by Django 2.0.8 on 2018-10-01 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0013_auto_20181001_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carreras',
            name='activado_crear',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
