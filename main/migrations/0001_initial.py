# Generated by Django 3.1.12 on 2025-01-04 07:47

import cloudinary.models
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
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
                ('thumbnail', cloudinary.models.CloudinaryField(max_length=255, verbose_name='thumbnail')),
                ('featured_video', cloudinary.models.CloudinaryField(max_length=255, verbose_name='featured_video')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('level', models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], default='Beginner', max_length=20)),
                ('duration', models.CharField(default='0', max_length=10)),
                ('category', models.CharField(default='uncategorized', max_length=255)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('requirements', models.TextField(default='', help_text='Enter the requirements for the course, separated by a comma.')),
                ('content', models.TextField(default='', help_text='Enter the course content, separated by a comma.')),
                ('lesson_title', models.CharField(default='Lesson', max_length=255)),
                ('lesson_video', cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='lesson_video')),
                ('instructor', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='courses', to=settings.AUTH_USER_MODEL)),
                ('students', models.ManyToManyField(blank=True, related_name='enrolled_courses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrolled_at', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CourseStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
