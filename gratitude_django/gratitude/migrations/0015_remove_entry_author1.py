# Generated by Django 2.0.5 on 2018-08-22 00:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gratitude', '0014_entry_author1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='author1',
        ),
    ]
