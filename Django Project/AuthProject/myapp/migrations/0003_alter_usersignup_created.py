# Generated by Django 4.1.4 on 2023-01-06 10:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_usersignup_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersignup',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 6, 16, 19, 3, 976807)),
        ),
    ]
