# Generated by Django 3.2.9 on 2021-12-08 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0002_receitas_pessoas'),
    ]

    operations = [
        migrations.AddField(
            model_name='receitas',
            name='publicada',
            field=models.BooleanField(default=False),
        ),
    ]
