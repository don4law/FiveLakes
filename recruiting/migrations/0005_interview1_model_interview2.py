# Generated by Django 5.0.1 on 2024-01-30 01:36

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiting', '0004_remove_interview1_id_interview1_applicant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interview1_Model',
            fields=[
                ('applicant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='recruiting.applicant')),
                ('interview1_scheduled', models.BooleanField(default=False, verbose_name='First Interview Scheduled')),
                ('interview1_date', models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='First Interview Date')),
                ('interviewer1_manager', models.CharField(blank=True, choices=[('Don Green', 'Don Green')], max_length=25, null=True, verbose_name='Interviewer')),
                ('interview1_completed', models.BooleanField(default=False, verbose_name='First Interview Completed')),
                ('interview1_notes', models.TextField(blank=True, max_length=255, null=True, verbose_name='Notes')),
            ],
            options={
                'verbose_name': 'First Interview',
                'verbose_name_plural': 'First Interview',
            },
        ),
        migrations.CreateModel(
            name='Interview2',
            fields=[
                ('applicant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='recruiting.applicant')),
                ('interview2_scheduled', models.BooleanField(default=False, verbose_name='First Interview Scheduled')),
            ],
            options={
                'verbose_name': 'Second Interview',
                'verbose_name_plural': 'Second Interview',
            },
        ),
    ]