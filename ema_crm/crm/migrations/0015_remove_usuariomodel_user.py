# Generated by Django 3.1.4 on 2020-12-16 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0014_auto_20201216_1540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuariomodel',
            name='user',
        ),
    ]
