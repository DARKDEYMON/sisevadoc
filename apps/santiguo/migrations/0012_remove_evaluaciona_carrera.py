# Generated by Django 2.0.8 on 2019-05-20 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('santiguo', '0011_evaluaciona_carrerasa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evaluaciona',
            name='carrera',
        ),
    ]
