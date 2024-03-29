# Generated by Django 3.1.3 on 2021-01-12 18:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crm', '0003_auto_20210112_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='GrupoDeApoyoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
            ],
        ),
        migrations.RenameModel(
            old_name='CuotasPagasModel',
            new_name='CuotaPagaModel',
        ),
        migrations.CreateModel(
            name='GrupoDeApoyoPacienteModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grupoDeApoyo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.grupodeapoyomodel')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.pacientemodel')),
            ],
        ),
        migrations.AddField(
            model_name='grupodeapoyomodel',
            name='pacientes',
            field=models.ManyToManyField(through='crm.GrupoDeApoyoPacienteModel', to='crm.PacienteModel'),
        ),
        migrations.AddField(
            model_name='pacientemodel',
            name='gruposDeApoyo',
            field=models.ManyToManyField(through='crm.GrupoDeApoyoPacienteModel', to='crm.GrupoDeApoyoModel'),
        ),
    ]
