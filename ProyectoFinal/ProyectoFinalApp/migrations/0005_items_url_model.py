# Generated by Django 4.0.5 on 2022-07-18 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoFinalApp', '0004_alter_items_imagen_alter_items_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='url_model',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
