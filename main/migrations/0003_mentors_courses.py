# Generated by Django 3.2.4 on 2021-07-29 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentors',
            name='courses',
            field=models.ManyToManyField(to='main.Courses'),
        ),
    ]
