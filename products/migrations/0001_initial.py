# Generated by Django 5.1.5 on 2025-02-04 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.URLField(max_length=500)),
                ('nome', models.CharField(max_length=255)),
                ('preco', models.FloatField()),
                ('parcelamento', models.IntegerField()),
                ('link', models.URLField(max_length=500)),
                ('preco_sem_desconto', models.FloatField()),
                ('percentual_desconto', models.FloatField()),
                ('tipo_entrega', models.CharField(choices=[('Full', 'Full'), ('Normal', 'Normal')], max_length=10)),
                ('frete_gratis', models.BooleanField(default=False)),
            ],
        ),
    ]
