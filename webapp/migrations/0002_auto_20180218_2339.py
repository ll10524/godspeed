# Generated by Django 2.0.2 on 2018-02-18 23:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactinfo',
            old_name='date',
            new_name='date_time',
        ),
    ]
