# Generated by Django 2.0.8 on 2019-03-07 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('santiguo', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='evaluaciona',
            unique_together={('docentea', 'gestion', 'sigla')},
        ),
    ]