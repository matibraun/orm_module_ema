# Generated by Django 3.1.3 on 2020-12-12 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0005_auto_20201211_1516'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SintomasModel',
            new_name='SintomaModel',
        ),
        migrations.RenameModel(
            old_name='TerapiasRehabilitacionModel',
            new_name='TerapiaRehabilitacionModel',
        ),
    ]
