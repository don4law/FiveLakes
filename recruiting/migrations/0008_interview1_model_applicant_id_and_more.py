# Generated by Django 5.0.1 on 2024-01-30 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiting', '0007_interview1_model_interview1_completed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='interview1_model',
            name='applicant_id',
            field=models.IntegerField(default=0, verbose_name='Applicant id'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='interview1_model',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]