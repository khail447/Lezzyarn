# Generated by Django 3.2.6 on 2021-08-21 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yarnerprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='yarnerprofile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]