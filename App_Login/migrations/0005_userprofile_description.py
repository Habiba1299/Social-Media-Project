# Generated by Django 4.0.1 on 2023-08-17 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0004_userprofile_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]