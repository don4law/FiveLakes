# Generated by Django 5.0.1 on 2024-02-07 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attorneys', '0019_remove_call_monitoring_model_author_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='call_monitoring_model',
            name='notes',
            field=models.TextField(blank=True, max_length=255, null=True, verbose_name='Notes'),
        ),
    ]