# Generated by Django 5.0.1 on 2024-01-30 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiting', '0011_rename_decline_to_continue_interview1_model_approve_to_continue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interview1_model',
            name='approve_to_continue',
            field=models.BooleanField(default=False, verbose_name='Approved to Continue'),
        ),
    ]
