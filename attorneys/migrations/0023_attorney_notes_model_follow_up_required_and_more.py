# Generated by Django 5.0.1 on 2024-02-08 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attorneys', '0022_alter_call_monitoring_model_call_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='attorney_notes_model',
            name='follow_up_required',
            field=models.BooleanField(default=False, verbose_name="f/u Req'd"),
        ),
        migrations.AlterField(
            model_name='attorney_notes_model',
            name='follow_up_notes',
            field=models.TextField(blank=True, max_length=255, null=True, verbose_name='Follow-Up Notes'),
        ),
    ]