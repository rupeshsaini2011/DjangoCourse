# Generated by Django 3.2.5 on 2021-09-01 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teaching', '0020_auto_20210901_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='institute',
            name='name',
            field=models.CharField(max_length=127, null=True),
        ),
    ]
