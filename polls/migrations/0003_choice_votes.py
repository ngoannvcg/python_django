# Generated by Django 2.1.dev20180405145536 on 2018-04-11 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_remove_choice_votes'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
