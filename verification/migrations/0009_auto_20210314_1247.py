# Generated by Django 3.1.7 on 2021-03-14 12:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verification', '0008_auto_20210314_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesstoken',
            name='token',
            field=models.TextField(blank=True, default=datetime.datetime(2021, 3, 14, 12, 47, 55, 619327), max_length=5000),
        ),
    ]
