# Generated by Django 4.2 on 2024-05-26 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_facturevente'),
    ]

    operations = [
        migrations.CreateModel(
            name='FactureAchat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_facture_achat', models.DateField()),
                ('montant_total_achat_TTC', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
