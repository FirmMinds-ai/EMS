# Generated by Django 3.2.7 on 2021-09-15 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portal', '0004_permanent_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permanent_address',
            name='empid',
            field=models.CharField(default='empid', max_length=30),
        ),
    ]