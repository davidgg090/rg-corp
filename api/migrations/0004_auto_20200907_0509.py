# Generated by Django 3.0.7 on 2020-09-07 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200906_0320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scraper',
            name='currency',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='scrapervalues',
            name='value',
            field=models.CharField(default=0, max_length=50),
        ),
    ]