# Generated by Django 5.0.1 on 2024-02-18 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attorneys', '0052_remove_call_monitoring_model_call_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='call_monitoring_model',
            name='call_datetime',
        ),
        migrations.AddField(
            model_name='call_monitoring_model',
            name='call_date',
            field=models.DateField(blank=True, max_length=25, null=True, verbose_name='Call Date'),
        ),
        migrations.AddField(
            model_name='call_monitoring_model',
            name='call_time',
            field=models.TimeField(blank=True, max_length=25, null=True, verbose_name='Call Time'),
        ),
    ]