# Generated by Django 3.0.4 on 2020-03-26 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20200313_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweets',
            name='tweetPlace',
            field=models.CharField(default='NA', max_length=1000, null=True),
        ),
    ]
