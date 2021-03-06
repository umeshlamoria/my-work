# Generated by Django 3.0 on 2019-12-15 16:37

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20191215_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='name',
        ),
        migrations.AddField(
            model_name='comment',
            name='approved_comments',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 15, 16, 37, 9, 845744, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='comment',
            name='mobile',
            field=models.IntegerField(default=False, max_length=12),
        ),
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.TextField(default=False),
        ),
        migrations.AddField(
            model_name='comment',
            name='website',
            field=models.URLField(blank=True, max_length=160),
        ),
        migrations.AlterField(
            model_name='categorie',
            name='utimestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 15, 16, 37, 9, 847064, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.Post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 15, 16, 37, 9, 843702, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tag',
            name='utimestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 15, 16, 37, 9, 847980, tzinfo=utc)),
        ),
    ]
