# Generated by Django 3.2.5 on 2021-09-01 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teaching', '0018_auto_20210901_1145'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='institution',
            new_name='institute',
        ),
        migrations.RemoveField(
            model_name='institute',
            name='name',
        ),
    ]