# Generated by Django 5.0.1 on 2024-01-30 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('states', '0002_alter_state_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='manager',
            field=models.CharField(blank=True, choices=[('Don Green', 'Don Green'), ('Jessica Most', 'Jessica Most')], max_length=50, null=True, verbose_name='Manager'),
        ),
    ]
