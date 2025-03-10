# Generated by Django 4.2.15 on 2024-09-06 14:59

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_article_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime.today),
        ),
        migrations.AlterField(
            model_name='article',
            name='summary',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
