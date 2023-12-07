# Generated by Django 4.2.7 on 2023-11-24 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=0)),
                ('precio_venta', models.FloatField(default=0.0)),
                ('descuento_por_cantidad', models.FloatField(default=0.0)),
                ('detalle_lote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.detallelote')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.usuario')),
            ],
        ),
    ]