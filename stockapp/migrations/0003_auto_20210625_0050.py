# Generated by Django 3.0.5 on 2021-06-24 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockapp', '0002_auto_20210624_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='stocklist',
            name='slug',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stocklist',
            name='industry',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='stocklist',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
