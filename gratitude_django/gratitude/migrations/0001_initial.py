# Generated by Django 2.0.5 on 2018-07-31 12:45

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason1', models.CharField(max_length=100)),
                ('reason2', models.CharField(max_length=100)),
                ('reason3', models.CharField(max_length=100)),
                ('goal', models.TextField(blank=True, null=True)),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('author', models.IntegerField()),
            ],
        ),
    ]
