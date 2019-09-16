# Generated by Django 2.0.2 on 2018-03-05 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydesign', '0004_auto_20180305_2010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_subscribe',
        ),
        migrations.AddField(
            model_name='user',
            name='subscribe',
            field=models.CharField(default='on', max_length=4, verbose_name='是否订阅电子杂志'),
        ),
    ]
