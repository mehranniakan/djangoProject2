# Generated by Django 3.2.25 on 2024-04-29 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_contact_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='Subject',
            field=models.CharField(max_length=255, null=True),
        ),
    ]