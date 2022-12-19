# Generated by Django 3.0.2 on 2022-12-19 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0010_auto_20221219_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='pago',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='pagoxHora',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=4),
        ),
    ]
