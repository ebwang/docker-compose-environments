# Generated by Django 3.2.9 on 2021-12-07 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0001_initial'),
        ('receitas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='receitas',
            name='pessoas',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='pessoas.pessoas'),
            preserve_default=False,
        ),
    ]
