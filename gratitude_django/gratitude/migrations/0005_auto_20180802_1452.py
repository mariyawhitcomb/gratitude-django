# Generated by Django 2.0.5 on 2018-08-02 14:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gratitude', '0004_auto_20180801_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to=settings.AUTH_USER_MODEL),
        ),
    ]
