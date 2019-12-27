# Generated by Django 3.0 on 2019-12-15 11:47

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20191214_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured',
            field=models.ImageField(blank=True, upload_to='featured'),
        ),
        migrations.AddField(
            model_name='post',
            name='keyword',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='meta_description',
            field=models.TextField(blank=True, verbose_name='meta description'),
        ),
        migrations.AddField(
            model_name='post',
            name='meta_title',
            field=models.CharField(blank=True, max_length=40, verbose_name='meta title'),
        ),
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='thumbnail'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='title',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='categories',
            name='utimestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 15, 11, 47, 41, 244829, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 15, 11, 47, 41, 243194, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='tag',
            name='utimestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 15, 11, 47, 41, 246492, tzinfo=utc)),
        ),
    ]
