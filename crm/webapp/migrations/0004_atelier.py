# Generated by Django 4.2 on 2024-05-26 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_transforma'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atelier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_atelier', models.CharField(max_length=255)),
                ('adresse_atelier', models.CharField(max_length=255)),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.produit')),
                ('transformation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.transforma')),
            ],
        ),
    ]
