# Generated by Django 3.1.3 on 2021-01-05 14:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crm', '0015_remove_usuariomodel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reunionmodel',
            name='paciente',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='crm.pacientemodel'),
        ),
        migrations.AlterField(
            model_name='reunionmodel',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
