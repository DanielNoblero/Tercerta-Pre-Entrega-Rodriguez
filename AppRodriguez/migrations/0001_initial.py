# Generated by Django 4.1.7 on 2023-03-14 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='buscar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Articulo', models.CharField(max_length=30)),
                ('Cantidad', models.CharField(max_length=30)),
                ('Precio', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Mayorista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreEmpresa', models.CharField(max_length=30)),
                ('Telefono', models.CharField(max_length=15)),
                ('Email', models.CharField(max_length=30)),
                ('Dni', models.CharField(max_length=10)),
                ('Direccion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Minorista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=30)),
                ('Apellido', models.CharField(max_length=30)),
                ('Telefono', models.CharField(max_length=15)),
                ('Email', models.CharField(max_length=30)),
                ('Dni', models.CharField(max_length=10)),
                ('Direccion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Articulo', models.CharField(max_length=30)),
                ('Cantidad', models.CharField(max_length=30)),
                ('Precio', models.CharField(max_length=15)),
            ],
        ),
    ]