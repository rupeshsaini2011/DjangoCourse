# Generated by Django 3.2.5 on 2021-07-21 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teaching', '0007_auto_20210714_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='is_popular',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='blog',
            name='context',
            field=models.TextField(),
        ),
    ]