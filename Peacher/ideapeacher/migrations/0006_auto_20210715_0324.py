# Generated by Django 3.1.5 on 2021-07-14 21:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideapeacher', '0005_category_idea'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 15, 3, 24, 8, 552867)),
        ),
    ]
