# Generated by Django 4.2.13 on 2024-05-17 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_remove_post_publish_time_alter_post_created_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Email', models.EmailField(max_length=254)),
                ('Subject', models.CharField(max_length=255)),
                ('Message', models.TextField()),
                ('Approved', models.BooleanField(default=False)),
                ('Created_Date', models.DateTimeField(auto_now_add=True)),
                ('Updated_Date', models.DateTimeField(auto_now=True)),
                ('Post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post')),
            ],
        ),
    ]
