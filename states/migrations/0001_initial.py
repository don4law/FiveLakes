# Generated by Django 5.0.1 on 2024-01-28 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state_abbrev', models.CharField(max_length=2, null=True, unique=True, verbose_name='State Abbreviation')),
                ('state_full', models.CharField(max_length=50, null=True, unique=True, verbose_name='State Name')),
                ('state_status', models.CharField(blank=True, choices=[('Red', 'Red'), ('Green', 'Green'), ('Other', 'Other'), ('Inactive', 'Inactive'), ('Not in Network', 'Not in Network')], default='Red', max_length=25, verbose_name='Status')),
                ('manager', models.CharField(blank=True, choices=[], max_length=50, null=True, verbose_name='Manager')),
                ('recruiting_status', models.CharField(blank=True, choices=[('Recruiting', 'Recruiting'), ('Pending', 'Pending'), ('Staffed', 'Staffed')], default='Recruiting', max_length=25, verbose_name='Recruiting Status')),
                ('state_priority', models.CharField(blank=True, choices=[('Critical', 'Critical'), ('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low'), ('None', 'None')], default='Critical', max_length=25, verbose_name='Priority')),
                ('full_time', models.BooleanField(default=True, verbose_name='Full Time')),
                ('part_time', models.BooleanField(default=False, verbose_name='Part Time')),
                ('of_counsel', models.BooleanField(default=False, verbose_name='Of Counsel')),
                ('floater', models.BooleanField(default=False, verbose_name='Floater')),
                ('FTE_actual', models.IntegerField(blank=True, default=0, verbose_name='Actual FTE')),
                ('FTE_est', models.IntegerField(blank=True, default=0, verbose_name='Estimated FTE')),
                ('full_time_actual', models.IntegerField(blank=True, default=0, verbose_name='Actual Full-Time')),
                ('full_time_est', models.IntegerField(blank=True, default=0, verbose_name='Est. Full-Time')),
                ('part_time_actual', models.IntegerField(blank=True, default=0, verbose_name='Actual Part-Time')),
                ('part_time_est', models.IntegerField(blank=True, default=0, verbose_name='Est. Part-Time')),
                ('of_counsel_actual', models.IntegerField(blank=True, default=0, verbose_name='Actual Of-Counsel')),
                ('of_counsel_est', models.IntegerField(blank=True, default=0, verbose_name='Est. Of-Counsel')),
                ('floater_actual', models.IntegerField(blank=True, default=0, verbose_name='Actual Floater')),
                ('floater_est', models.IntegerField(blank=True, default=0, verbose_name='Estimated Floater')),
            ],
            options={
                'verbose_name': 'State Profile',
                'verbose_name_plural': 'State Profiles',
            },
        ),
    ]
