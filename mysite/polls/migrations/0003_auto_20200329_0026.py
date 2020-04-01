# Generated by Django 3.0.4 on 2020-03-29 00:26

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_question_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
                ('role', models.SmallIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='poll',
            name='close_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 5, 0, 26, 3, 548259, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='poll',
            name='open_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 29, 0, 26, 58, 481428, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.SmallIntegerField(default='0'),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=16)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='polls.User')),
            ],
        ),
        migrations.AddField(
            model_name='poll',
            name='allowed_users',
            field=models.ManyToManyField(to='polls.User'),
        ),
    ]