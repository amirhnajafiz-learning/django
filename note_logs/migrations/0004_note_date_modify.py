# Generated by Django 3.1 on 2020-09-24 06:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note_logs', '0003_notepad_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='date_modify',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 24, 6, 45, 30, 53374)),
            preserve_default=False,
        ),
    ]
