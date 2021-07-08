# Generated by Django 3.2.5 on 2021-07-06 05:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('blog_subject', models.CharField(max_length=127)),
                ('context', models.TextField(blank=True, null=True)),
                ('name', models.CharField(max_length=127)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=127)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127)),
                ('price', models.DecimalField(decimal_places=2, max_digits=11)),
                ('is_popular', models.BooleanField(default=False)),
                ('curriculum', models.TextField()),
                ('duration', models.PositiveSmallIntegerField(default=3)),
                ('lectures', models.PositiveSmallIntegerField(default=10)),
                ('quizzes', models.PositiveSmallIntegerField(default=5)),
                ('pass_percentage', models.DecimalField(decimal_places=2, default=50, max_digits=12)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_courses', to='teaching.category')),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127)),
                ('address', models.CharField(max_length=127)),
                ('contact', models.SmallIntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_institute', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(blank=True, null=True)),
                ('name', models.CharField(max_length=127)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.SmallIntegerField()),
                ('about', models.TextField(blank=True, null=True)),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to='teaching.institute')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_teacher', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_subjects', to='teaching.course')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.SmallIntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_student', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=11)),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=12)),
                ('time_from', models.TimeField()),
                ('time_to', models.TimeField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_schedules', to='teaching.course')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject_schedules', to='teaching.subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_schedules', to='teaching.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('assignment', models.TextField()),
                ('link', models.URLField()),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule_periods', to='teaching.schedule')),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=127)),
                ('payment_id', models.CharField(max_length=127)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=11)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_enrollments', to='teaching.course')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='currency_enrollments', to='teaching.currency')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_enrollments', to='teaching.student')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='currency_courses', to='teaching.currency'),
        ),
        migrations.AddField(
            model_name='course',
            name='institution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='institutes', to='teaching.institute'),
        ),
        migrations.AddField(
            model_name='course',
            name='main_teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_courses', to='teaching.teacher'),
        ),
    ]
