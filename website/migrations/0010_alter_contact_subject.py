# Generated by Django 3.2.25 on 2024-04-30 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_alter_contact_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='Subject',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]