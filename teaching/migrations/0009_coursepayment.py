# Generated by Django 3.2.5 on 2021-07-27 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teaching', '0008_auto_20210721_0941'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoursePayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseorder_id', models.CharField(blank=True, max_length=127)),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=127)),
                ('paid', models.BooleanField(default=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_name', to='teaching.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_user', to='teaching.student')),
            ],
        ),
    ]
