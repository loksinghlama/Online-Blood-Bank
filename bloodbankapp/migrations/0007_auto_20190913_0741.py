# Generated by Django 2.2.5 on 2019-09-13 01:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodbankapp', '0006_donated_donate_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestclass',
            name='dateline_request',
            field=models.DateField(default=datetime.date(2019, 9, 13)),
        ),
    ]
