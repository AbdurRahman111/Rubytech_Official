# Generated by Django 3.2 on 2023-02-04 13:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20230204_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs_table',
            name='Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 4, 19, 44, 43, 326797)),
        ),
    ]
