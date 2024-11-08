# Generated by Django 5.0.1 on 2024-02-09 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('states', '0004_alter_state_manager'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='state',
            name='FTE_actual',
        ),
        migrations.RemoveField(
            model_name='state',
            name='floater_actual',
        ),
        migrations.RemoveField(
            model_name='state',
            name='full_time_actual',
        ),
        migrations.RemoveField(
            model_name='state',
            name='of_counsel_actual',
        ),
        migrations.RemoveField(
            model_name='state',
            name='part_time_actual',
        ),
        migrations.AlterField(
            model_name='state',
            name='manager',
            field=models.CharField(blank=True, choices=[('Don Green', 'Don Green'), ('Eric Peterson', 'Eric Peterson'), ('Jessica Most', 'Jessica Most'), ('Matt Barnes', 'Matt Barnes')], max_length=50, null=True, verbose_name='Manager'),
        ),
    ]
