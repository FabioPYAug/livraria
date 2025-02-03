# Generated by Django 5.1.3 on 2025-02-03 12:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0015_compra_data_compra_tipo_pagamento_itenscompra_preco"),
    ]

    operations = [
        migrations.AlterField(
            model_name="itenscompra",
            name="livro",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, related_name="itens_compra", to="core.livro"
            ),
        ),
    ]
