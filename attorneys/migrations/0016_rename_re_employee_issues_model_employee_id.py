# Generated by Django 5.0.1 on 2024-02-27 01:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attorneys', '0015_remove_issues_model_employee_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issues_model',
            old_name='re_employee',
            new_name='employee_id',
        ),
    ]