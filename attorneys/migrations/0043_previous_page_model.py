# Generated by Django 5.0.1 on 2024-02-15 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attorneys', '0042_alter_attorney_notes_model_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Previous_Page_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('previous_page', models.CharField(blank=True, max_length=20, null=True, verbose_name='Previous Page')),
            ],
            options={
                'verbose_name': 'Previous Page',
                'verbose_name_plural': 'Previous Page',
            },
        ),
    ]