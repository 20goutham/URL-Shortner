# Generated by Django 5.1.1 on 2024-10-19 06:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_longtoshort_date_alter_longtoshort_short_url_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clickanalytics',
            name='date',
        ),
        migrations.AlterField(
            model_name='clickanalytics',
            name='device',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='clickanalytics',
            name='url',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='click_analytics', to='myapp.longtoshort'),
        ),
        migrations.AlterField(
            model_name='longtoshort',
            name='short_url',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
