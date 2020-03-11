# Generated by Django 3.0.2 on 2020-03-06 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweets',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('tweetText', models.CharField(default='NA', max_length=200, null=True)),
                ('user', models.CharField(default='NA', max_length=200, null=True)),
                ('followers', models.IntegerField(default='NA', null=True)),
                ('date', models.DateTimeField(default='NA', max_length=200, null=True)),
                ('location', models.CharField(default='NA', max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TweetsCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default='NA', null=True)),
                ('date', models.DateTimeField(default='2012-09-04 06:00:00', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
    ]