# Generated by Django 3.1.4 on 2021-01-06 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0025_auto_20210106_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='tallermodel',
            name='pacientes',
            field=models.ManyToManyField(to='crm.PacienteModel'),
        ),
    ]
