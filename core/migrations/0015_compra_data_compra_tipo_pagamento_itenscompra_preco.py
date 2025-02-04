# Generated by Django 5.1.3 on 2024-12-19 14:03

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0014_itenscompra"),
    ]

    operations = [
        migrations.AddField(
            model_name="compra",
            name="data",
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="compra",
            name="tipo_pagamento",
            field=models.IntegerField(
                choices=[
                    (1, "Cartão de Crédito"),
                    (2, "Cartão de Débito"),
                    (3, "PIX"),
                    (4, "Boleto"),
                    (5, "Transferência Bancária"),
                    (6, "Dinheiro"),
                    (7, "Outro"),
                ],
                default=1,
            ),
        ),
        migrations.AddField(
            model_name="itenscompra",
            name="preco",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
