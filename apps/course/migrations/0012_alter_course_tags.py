# Generated by Django 4.1.1 on 2022-11-08 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_author'),
        ('course', '0011_alter_lesson_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='tags',
            field=models.ManyToManyField(blank=True, to='blog.tag'),
        ),
    ]
