# Generated by Django 3.2.7 on 2021-09-26 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portal', '0011_task_task_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee_profile',
            name='profile_img',
            field=models.ImageField(blank=True, upload_to='Portal/images/'),
        ),
    ]
