# Generated by Django 2.0.5 on 2018-08-02 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gratitude', '0006_auto_20180802_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='gratitude.Entry'),
        ),
    ]
