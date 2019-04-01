# Generated by Django 2.0.8 on 2019-03-11 21:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_auto_20190311_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_docente',
            name='celular',
            field=models.IntegerField(default=77777777, validators=[django.core.validators.MaxValueValidator(99999999), django.core.validators.MinValueValidator(11111111)]),
            preserve_default=False,
        ),
    ]