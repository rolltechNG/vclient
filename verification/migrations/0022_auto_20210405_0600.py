# Generated by Django 3.1.7 on 2021-04-05 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verification', '0021_auto_20210326_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='direction',
            field=models.CharField(blank=True, choices=[('credit', 'CREDIT'), ('debit', 'DEBIT')], default='credit', editable=False, max_length=100, null=True),
        ),
    ]
