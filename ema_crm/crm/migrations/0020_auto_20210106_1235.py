# Generated by Django 3.1.4 on 2021-01-06 15:35

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crm', '0019_usuariomodel_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UsuarioModel',
            new_name='UsuarioExtendidoModel',
        ),
    ]
