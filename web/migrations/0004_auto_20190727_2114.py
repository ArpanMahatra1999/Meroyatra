# Generated by Django 2.0.8 on 2019-07-27 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20190727_1348'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='blog',
            new_name='description',
        ),
    ]
