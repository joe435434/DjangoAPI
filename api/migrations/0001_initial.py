# Generated by Django 5.1.2 on 2024-10-25 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('usuario_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_usuario', models.CharField(max_length=255)),
            ],
        ),
    ]
