# Generated by Django 2.2.7 on 2019-11-12 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nxtwatch', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratings',
            name='userid',
            field=models.TextField(blank=True, null=True),
        ),
    ]
