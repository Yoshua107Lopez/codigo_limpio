# Generated by Django 4.2.3 on 2023-09-29 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cliente', models.CharField(max_length=255)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]