# Generated by Django 2.0.5 on 2018-08-01 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gratitude', '0003_auto_20180801_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='author',
            field=models.IntegerField(),
        ),
    ]