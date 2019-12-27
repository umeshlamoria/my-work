# Generated by Django 3.0 on 2019-12-13 12:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=40)),
                ('content', models.TextField()),
                ('utimestamp', models.DateTimeField(default=datetime.datetime(2019, 12, 13, 12, 39, 43, 735718, tzinfo=utc))),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 13, 12, 39, 43, 734702, tzinfo=utc)),
        ),
    ]