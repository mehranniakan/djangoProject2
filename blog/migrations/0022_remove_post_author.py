# Generated by Django 4.2.13 on 2024-06-02 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='Author',
        ),
    ]
