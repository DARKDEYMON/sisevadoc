# Generated by Django 2.0.8 on 2019-05-16 15:33

from django.db import migrations, models

def forward(apps, schema_editor):
    evaluaciona = apps.get_model("santiguo", "evaluaciona")
    carrerasa = apps.get_model("santiguo", "carrerasa")
    res = evaluaciona.objects.values_list('carrera',flat = True).distinct()
    for a in res:
        carrerasa.objects.create(nombre=str(a))

class Migration(migrations.Migration):

    dependencies = [
        ('santiguo', '0009_plan_mejorasa_ultimo_generado'),
    ]

    operations = [
        migrations.CreateModel(
            name='carrerasa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.RunPython(forward)
    ]
