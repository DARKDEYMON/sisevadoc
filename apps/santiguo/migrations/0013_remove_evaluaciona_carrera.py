# Generated by Django 2.0.8 on 2019-05-20 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('santiguo', '0012_auto_20190520_1539'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evaluaciona',
            name='carrera',
        ),
    ]
