# Generated by Django 4.0.5 on 2022-07-18 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoFinalApp', '0005_items_url_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='url_model',
            field=models.URLField(max_length=250),
        ),
    ]
