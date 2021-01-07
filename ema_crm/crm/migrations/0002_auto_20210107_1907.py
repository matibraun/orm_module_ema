# Generated by Django 3.1.4 on 2021-01-07 22:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='CoberturaMedicaModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='ComposicionFamiliarModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vinculo', models.CharField(max_length=300)),
                ('nombre', models.CharField(max_length=300)),
                ('apellido', models.CharField(max_length=300)),
                ('fechaNacimiento', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('telFijo', models.CharField(blank=True, max_length=300, null=True)),
                ('telMovil', models.CharField(max_length=300)),
                ('ocupacion', models.CharField(max_length=300)),
                ('esConviviente', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='DiagnosticoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='DomicilioModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle', models.CharField(max_length=300)),
                ('numero', models.CharField(max_length=300)),
                ('piso', models.CharField(blank=True, max_length=300, null=True)),
                ('localidad', models.CharField(max_length=300)),
                ('codigoPostal', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='FormaClinicaModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='PacienteModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=300, unique=True)),
                ('nombre', models.CharField(max_length=300)),
                ('apellido', models.CharField(max_length=300)),
                ('fechaNacimiento', models.DateField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telFijo', models.CharField(blank=True, max_length=300, null=True)),
                ('telMovil', models.CharField(max_length=300)),
                ('fechaAlta', models.DateField(auto_now=True)),
                ('areaALaQueSeDerivo', models.IntegerField()),
                ('esSocio', models.BooleanField(default=False)),
                ('fechaAsociacion', models.DateField(blank=True, null=True)),
                ('fechaUltimaCuotaPaga', models.DateField(blank=True, null=True)),
                ('recibeMailing', models.BooleanField(default=False)),
                ('coberturaMedica', models.IntegerField()),
                ('lugarDeAtencion', models.CharField(max_length=300)),
                ('neurologoCabecera', models.CharField(max_length=300)),
                ('participaGrupoApoyoPacientes', models.BooleanField(default=False)),
                ('participaGrupoApoyoFamiliares', models.BooleanField(default=False)),
                ('fechaDiagnostico', models.DateField()),
                ('actividadFisica', models.BooleanField(default=False)),
                ('fumadorTabaco', models.BooleanField(default=False)),
                ('antecedentesEnfermedades', models.CharField(blank=True, max_length=300, null=True)),
                ('tieneCUD', models.BooleanField(default=False)),
                ('fechaVencimientoCUD', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProvinciaModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='ReunionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now=True)),
                ('contenido', models.TextField()),
                ('areaAlQueSeDerivo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='crm.areamodel')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.pacientemodel')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SintomaModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='SituacionHabitacionalModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='SituacionLaboralModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='TallerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='TallerPacienteModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.pacientemodel')),
                ('taller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.tallermodel')),
            ],
        ),
        migrations.CreateModel(
            name='TerapiaRehabilitacionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='TratamientoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now=True)),
                ('medicoTratante', models.CharField(max_length=300)),
                ('tratamiento', models.CharField(max_length=300)),
                ('droga', models.CharField(max_length=300)),
                ('marca', models.CharField(max_length=300)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.pacientemodel')),
                ('usuarioQueCargoTratamiento', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioExtendidoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=300)),
                ('fechaNacimiento', models.DateField()),
                ('telFijo', models.CharField(blank=True, max_length=300, null=True)),
                ('telMovil', models.CharField(max_length=300)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='crm.areamodel')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Paciente',
        ),
        migrations.AddField(
            model_name='tallermodel',
            name='pacientes',
            field=models.ManyToManyField(through='crm.TallerPacienteModel', to='crm.PacienteModel'),
        ),
        migrations.AddField(
            model_name='pacientemodel',
            name='talleres',
            field=models.ManyToManyField(through='crm.TallerPacienteModel', to='crm.TallerModel'),
        ),
        migrations.AddField(
            model_name='pacientemodel',
            name='usuarioQueRealizoAlta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='domiciliomodel',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.pacientemodel'),
        ),
        migrations.AddField(
            model_name='domiciliomodel',
            name='provincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='crm.provinciamodel'),
        ),
        migrations.AddField(
            model_name='composicionfamiliarmodel',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.pacientemodel'),
        ),
    ]
