# Generated by Django 3.0 on 2019-12-15 16:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20191215_1620'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='website',
        ),
        migrations.AlterField(
            model_name='categorie',
            name='utimestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 15, 16, 24, 1, 59665, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 15, 16, 24, 1, 56596, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tag',
            name='utimestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 15, 16, 24, 1, 62236, tzinfo=utc)),
        ),
    ]
