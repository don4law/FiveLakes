# Generated by Django 5.0.1 on 2024-02-19 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attorneys', '0058_alter_hr_requests_model_approval_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attorney_notes_model',
            name='date',
            field=models.DateField(blank=True, default='02/19/2024', max_length=25, null=True, verbose_name='Review Date'),
        ),
        migrations.AlterField(
            model_name='call_monitoring_model',
            name='date',
            field=models.DateField(blank=True, default='02/19/2024', max_length=25, null=True, verbose_name='Review Date'),
        ),
        migrations.AlterField(
            model_name='hr_requests_model',
            name='date',
            field=models.DateField(blank=True, default='02/19/2024', max_length=25, null=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='qa_model',
            name='qa_date',
            field=models.DateField(blank=True, default='02/19/2024', max_length=25, null=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='search_attorneys_model',
            name='search_manager',
            field=models.CharField(blank=True, choices=[('Don Green', 'Don Green'), ('Eric Peterson', 'Eric Peterson'), ('Jessica Most', 'Jessica Most'), ('Kevin Zibolski', 'Kevin Zibolski'), ('Matt Barnes', 'Matt Barnes')], max_length=25, null=True, verbose_name='Search by Manager'),
        ),
        migrations.AlterField(
            model_name='to_do_model',
            name='date',
            field=models.DateField(blank=True, default='02/19/2024', max_length=25, null=True, verbose_name='Date'),
        ),
    ]