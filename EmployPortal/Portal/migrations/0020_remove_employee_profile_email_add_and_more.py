# Generated by Django 4.0.4 on 2022-04-16 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portal', '0019_alter_loginauthentication_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee_profile',
            name='email_add',
        ),
        migrations.RemoveField(
            model_name='employee_profile',
            name='emp_first_name',
        ),
        migrations.RemoveField(
            model_name='employee_profile',
            name='emp_last_name',
        ),
        migrations.RemoveField(
            model_name='employee_profile',
            name='emp_midle_name',
        ),
        migrations.AddField(
            model_name='employee_profile',
            name='email',
            field=models.EmailField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='employee_profile',
            name='emp_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='employee_profile',
            name='blood_gruop',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='employee_profile',
            name='contact_no',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='employee_profile',
            name='department',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='employee_profile',
            name='designation',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='employee_profile',
            name='pancard_no',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='employee_profile',
            name='username',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='employee_profile',
            name='userpassword',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]