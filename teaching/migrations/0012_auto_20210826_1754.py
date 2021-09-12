# Generated by Django 3.2.5 on 2021-08-26 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teaching', '0011_auto_20210825_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_enrollment', to='teaching.course'),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='currency_enrollment', to='teaching.currency'),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=11),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_enrollment', to='teaching.student'),
        ),
    ]
