# Generated by Django 3.0 on 2019-12-16 11:34

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20191216_0751'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='blog.Comment'),
        ),
        migrations.AlterField(
            model_name='categorie',
            name='utimestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 16, 11, 34, 55, 625539, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 16, 11, 34, 55, 624151, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 16, 11, 34, 55, 622192, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tag',
            name='utimestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 16, 11, 34, 55, 626461, tzinfo=utc)),
        ),
    ]
