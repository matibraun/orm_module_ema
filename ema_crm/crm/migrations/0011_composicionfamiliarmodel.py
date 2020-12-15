# Generated by Django 3.1.4 on 2020-12-15 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0010_auto_20201215_1839'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComposicionFamiliarModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vinculo', models.CharField(max_length=300)),
                ('nombre', models.CharField(max_length=300)),
                ('apellido', models.CharField(max_length=300)),
                ('fechaNacimiento', models.DateField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telFijo', models.CharField(blank=True, max_length=300, null=True)),
                ('telMovil', models.CharField(max_length=300)),
                ('ocupacion', models.CharField(max_length=300)),
                ('esConviviente', models.BooleanField(default=False)),
            ],
        ),
    ]