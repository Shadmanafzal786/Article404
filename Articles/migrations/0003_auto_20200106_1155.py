# Generated by Django 2.2.3 on 2020-01-06 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0002_comments_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='category',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='Gaming', max_length=100),
        ),
    ]