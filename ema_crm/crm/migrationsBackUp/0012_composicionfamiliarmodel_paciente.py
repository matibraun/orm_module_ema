# Generated by Django 3.1.4 on 2020-12-15 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0011_composicionfamiliarmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='composicionfamiliarmodel',
            name='paciente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='crm.pacientemodel'),
            preserve_default=False,
        ),
    ]
