# Generated by Django 5.1.1 on 2024-11-05 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimentacao',
            name='data',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
