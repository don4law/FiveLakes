# Generated by Django 5.0.1 on 2024-01-31 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiting', '0019_finalstep_model_alter_applicant_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finalstep_model',
            name='offer_accepted',
            field=models.BooleanField(default=False, verbose_name='Offer Accepted and Signed'),
        ),
        migrations.AlterField(
            model_name='finalstep_model',
            name='offer_letter_email_date',
            field=models.DateField(blank=True, null=True, verbose_name='Offer Letter Date'),
        ),
        migrations.AlterField(
            model_name='finalstep_model',
            name='offer_letter_sent_charles',
            field=models.BooleanField(default=False, verbose_name='Offer Letter Emailed Chief Counsel'),
        ),
        migrations.AlterField(
            model_name='finalstep_model',
            name='start_date',
            field=models.DateField(blank=True, null=True, verbose_name='Start Date'),
        ),
    ]