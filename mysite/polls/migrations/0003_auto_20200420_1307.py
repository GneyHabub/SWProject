# Generated by Django 3.0.4 on 2020-04-20 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20200408_1559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='group',
        ),
        migrations.AddField(
            model_name='group',
            name='degree',
            field=models.CharField(choices=[('BS', 'Bachelor'), ('MS', 'Master')], default='BS', max_length=2),
        ),
        migrations.AddField(
            model_name='group',
            name='group_number',
            field=models.CharField(default='03', max_length=2),
        ),
        migrations.AddField(
            model_name='group',
            name='starting_year',
            field=models.CharField(default='18', max_length=2),
        ),
        migrations.AddField(
            model_name='group',
            name='track',
            field=models.CharField(choices=[('DS', 'Data Science'), ('SE', 'Software Engineering'), ('SNE', 'Security and Networks Engineering'), ('AIR', 'Robotics'), ('-', 'No track')], default='-', max_length=3),
        ),
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.SmallIntegerField(choices=[(0, 'Single choice'), (1, 'Multichoice'), (2, 'Input text')], default='0'),
        ),
    ]