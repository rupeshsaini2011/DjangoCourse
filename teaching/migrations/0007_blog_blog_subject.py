# Generated by Django 3.2.4 on 2021-06-25 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teaching', '0006_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_subject',
            field=models.CharField(default=1, max_length=127),
            preserve_default=False,
        ),
    ]
