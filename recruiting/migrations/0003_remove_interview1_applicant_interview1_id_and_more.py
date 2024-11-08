# Generated by Django 5.0.1 on 2024-01-28 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiting', '0002_alter_applicant_manager_alter_applicant_state_abbrev_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interview1',
            name='applicant',
        ),
        migrations.AddField(
            model_name='interview1',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='applicant',
            name='manager',
            field=models.CharField(blank=True, choices=[('Don Green', 'Don Green')], default='', max_length=50, verbose_name='Manager'),
        ),
    ]
