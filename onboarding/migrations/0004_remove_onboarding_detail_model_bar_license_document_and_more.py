# Generated by Django 5.0.1 on 2024-02-13 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onboarding', '0003_onboarding_detail_model_send_spreadsheet_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='onboarding_detail_model',
            name='bar_license_document',
        ),
        migrations.AlterField(
            model_name='onboarding_detail_model',
            name='save_license',
            field=models.BooleanField(default=False, verbose_name='Save bar license'),
        ),
    ]
