# Generated by Django 5.0.1 on 2024-02-07 19:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attorneys', '0016_off_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='HR_Requests_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, default='02/07/2024', max_length=25, null=True, verbose_name='Date')),
                ('time', models.TimeField(blank=True, max_length=25, null=True, verbose_name='Time')),
                ('request_type', models.CharField(choices=[('Flex', 'Flex'), ('PTO', 'PTO'), ('UTO', 'UTO'), ('Other', 'Other')], max_length=25, null=True, verbose_name='Request Type')),
                ('request_note', models.CharField(blank=True, max_length=255, null=True, verbose_name='Request Notes')),
                ('approved', models.BooleanField(default=False, verbose_name='Approved')),
                ('denied', models.BooleanField(default=False, verbose_name='Denied')),
                ('document', models.FileField(blank=True, null=True, upload_to='HR/')),
                ('reasoning', models.CharField(blank=True, max_length=255, null=True, verbose_name='Reasoning')),
                ('decision_manager', models.CharField(choices=[('Don Green', 'Don Green'), ('Jessica Most', 'Jessica Most'), ('Matt Barnes', 'Matt Barnes')], max_length=50, null=True, verbose_name='Decision Manager')),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attorneys.employee')),
            ],
            options={
                'verbose_name': 'Flex and PTO/UTO Tracking',
                'verbose_name_plural': 'Flex and PTO/UTO Tracking',
            },
        ),
        migrations.DeleteModel(
            name='Off_Model',
        ),
    ]