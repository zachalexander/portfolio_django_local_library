# Generated by Django 3.0.5 on 2020-04-18 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweets',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('tweetId', models.CharField(default='NA', max_length=1000, null=True)),
            ],
        ),
    ]
