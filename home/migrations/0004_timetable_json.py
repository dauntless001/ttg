# Generated by Django 4.0.5 on 2022-07-11 13:53

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_timetable_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='json',
            field=jsonfield.fields.JSONField(default={}),
            preserve_default=False,
        ),
    ]
