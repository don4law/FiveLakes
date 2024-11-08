# Generated by Django 5.0.1 on 2024-02-21 14:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Employee ID')),
                ('is_active', models.BooleanField(blank=True, default=True, null=True, verbose_name='Is Active')),
                ('state_abbrev', models.CharField(choices=[], max_length=25, null=True, verbose_name='State')),
                ('position', models.CharField(blank=True, choices=[('Full-Time', 'Full-Time'), ('Part-Time', 'Part-Time'), ('Of Counsel', 'Of Counsel'), ('Floater', 'Floater')], default='Full-Time', max_length=25, verbose_name='Position')),
                ('salary', models.CharField(default='80,000', max_length=10, verbose_name='Salary')),
                ('manager', models.CharField(blank=True, choices=[], default='', max_length=50, verbose_name='Manager')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, null=True, verbose_name='Gender')),
                ('first_name', models.CharField(max_length=25, verbose_name='First Name')),
                ('middle_name', models.CharField(blank=True, max_length=25, verbose_name='Middle Name')),
                ('last_name', models.CharField(max_length=25, verbose_name='Last Name')),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Phone Number')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('five_lakes_firm', models.BooleanField(default=True, verbose_name='Five Lakes Law Group')),
                ('huron_firm', models.BooleanField(default=False, verbose_name='Huron Law Group')),
                ('resume', models.FileField(blank=True, null=True, upload_to='resumes/')),
                ('hire_date', models.DateField(blank=True, max_length=255, null=True, verbose_name='Start Date')),
                ('start_date', models.DateField(max_length=255, null=True, verbose_name='Start Date')),
                ('onboarding_step', models.CharField(blank=True, max_length=50, null=True, verbose_name='Last Name')),
                ('onboarding_complete', models.BooleanField(default=False, verbose_name='Onboarding Complete')),
                ('priority', models.CharField(choices=[('Critical', 'Critical'), ('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], default='Low', max_length=10, null=True, verbose_name='Criticality Level')),
                ('prev_page', models.CharField(blank=True, max_length=100, null=True, verbose_name='Last Name')),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
            },
        ),
        migrations.CreateModel(
            name='Employee_More_Model',
            fields=[
                ('employee_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Employee ID')),
                ('address1', models.CharField(blank=True, max_length=50, null=True, verbose_name='Address1')),
                ('address2', models.CharField(blank=True, max_length=50, null=True, verbose_name='Address2')),
                ('city', models.CharField(blank=True, max_length=50, null=True, verbose_name='City')),
                ('resident_state', models.CharField(blank=True, max_length=5, null=True, verbose_name='State')),
                ('zip', models.CharField(blank=True, max_length=25, null=True, verbose_name='Zip')),
                ('phone2', models.CharField(blank=True, max_length=15, null=True, verbose_name='Phone Number2')),
                ('phone3', models.CharField(blank=True, max_length=15, null=True, verbose_name='Phone Number3')),
                ('email2', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email2')),
                ('email3', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email3')),
                ('state_bar_number', models.CharField(blank=True, max_length=25, null=True, verbose_name='State Bar Number')),
                ('state_bar_document', models.FileField(blank=True, null=True, upload_to='Bar/')),
                ('other_states', models.CharField(blank=True, max_length=25, null=True, verbose_name='Other States')),
                ('signed_offer_letter', models.FileField(blank=True, null=True, upload_to='HR/')),
                ('ICA_agreement', models.FileField(blank=True, null=True, upload_to='HR/')),
            ],
            options={
                'verbose_name': "Employee's Additional Data",
                'verbose_name_plural': "Employees' Additional Data",
            },
        ),
        migrations.CreateModel(
            name='Search_Attorneys_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_manager', models.CharField(blank=True, choices=[('Don Green', 'Don Green'), ('Eric Peterson', 'Eric Peterson'), ('Jessica Most', 'Jessica Most'), ('Kevin Zibolski', 'Kevin Zibolski'), ('Matt Barnes', 'Matt Barnes')], max_length=25, null=True, verbose_name='Search by Manager')),
                ('search_state', models.CharField(blank=True, choices=[], max_length=25, null=True, verbose_name='Search by State')),
                ('search_priority', models.CharField(blank=True, choices=[('Critical', 'Critical'), ('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], max_length=25, null=True, verbose_name='Search by Priority')),
            ],
            options={
                'verbose_name': 'Search',
                'verbose_name_plural': 'Search',
            },
        ),
        migrations.CreateModel(
            name='Call_Monitoring_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, default='02/21/2024', max_length=25, null=True, verbose_name='Review Date')),
                ('call_date', models.DateField(blank=True, max_length=25, null=True, verbose_name='Call Date')),
                ('call_time', models.TimeField(blank=True, max_length=25, null=True, verbose_name='Call Time')),
                ('duration', models.CharField(blank=True, max_length=25, null=True, verbose_name='Duration')),
                ('disposition', models.CharField(choices=[('None', 'None'), ('Left Voicemail', 'Left Voicemail'), ('Incomplete Consult', 'Incomplete Consult'), ('Credit Concerns', 'Credit Concerns'), ('Lawsuit Concerns', 'Lawsuit Concerns'), ('Requested Cancellation', 'Requested Cancellation'), ('No Answer', 'No Answer'), ('Cancellation Prior to Consult', 'Cancellation Prior to Consult')], max_length=50, null=True, verbose_name='Disposition')),
                ('notes', models.TextField(blank=True, max_length=255, null=True, verbose_name='Call Notes')),
                ('document', models.FileField(blank=True, null=True, upload_to='Calls/')),
                ('reviewer', models.CharField(choices=[], max_length=50, null=True, verbose_name='Reviewer')),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attorneys.employee')),
            ],
            options={
                'verbose_name': 'Call Monitoring',
                'verbose_name_plural': 'Call Monitoring',
            },
        ),
        migrations.CreateModel(
            name='Attorney_Notes_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, default='02/21/2024', max_length=25, null=True, verbose_name='Review Date')),
                ('from_person', models.CharField(blank=True, max_length=50, null=True, verbose_name='From (Name)')),
                ('notes', models.TextField(blank=True, max_length=255, null=True, verbose_name='Notes / Messages')),
                ('document', models.FileField(blank=True, null=True, upload_to='Notes/')),
                ('follow_up_required', models.BooleanField(default=False, verbose_name='Follow-up')),
                ('follow_up_notes', models.TextField(blank=True, max_length=255, null=True, verbose_name='Follow-Up Notes')),
                ('follow_up_completed', models.BooleanField(default=False, verbose_name='Completed')),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attorneys.employee')),
            ],
            options={
                'verbose_name': 'Attorney Notes',
                'verbose_name_plural': 'Attorney Notes',
            },
        ),
        migrations.CreateModel(
            name='HR_Requests_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, default='02/21/2024', max_length=25, null=True, verbose_name='Date')),
                ('time', models.TimeField(blank=True, max_length=25, null=True, verbose_name='Time')),
                ('request_type', models.CharField(choices=[('Flex', 'Flex'), ('PTO', 'PTO'), ('UTO', 'UTO'), ('Other', 'Other')], max_length=25, null=True, verbose_name='Request Type')),
                ('request_note', models.CharField(blank=True, max_length=255, null=True, verbose_name='Request Notes')),
                ('approval_status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Denied', 'Denied')], default='Pending', max_length=25, null=True, verbose_name='Request Status')),
                ('document', models.FileField(blank=True, null=True, upload_to='HR/')),
                ('reasoning', models.CharField(blank=True, max_length=255, null=True, verbose_name='Decision Reasoning')),
                ('decision_manager', models.CharField(choices=[], max_length=50, null=True, verbose_name='Decision Manager')),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attorneys.employee')),
            ],
            options={
                'verbose_name': 'Flex and PTO/UTO Tracking',
                'verbose_name_plural': 'Flex and PTO/UTO Tracking',
            },
        ),
        migrations.CreateModel(
            name='Metrics_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(max_length=25, null=True, verbose_name='Metric Date')),
                ('metric', models.CharField(choices=[('Attrition Rate', 'Attrition Rate'), ('Call Timeliness', 'Call Timeliness'), ('Review Completion', 'Review Completion'), ('EA Completion', 'EA Completion'), ('Pro Se Answer Reviews', 'Pro Se Answer Reviews'), ('Other', 'Other')], max_length=25, null=True, verbose_name='Metric')),
                ('other_description', models.CharField(blank=True, max_length=50, null=True, verbose_name='Metric')),
                ('value', models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='Value')),
                ('document', models.FileField(blank=True, null=True, upload_to='Metrics/')),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attorneys.employee')),
            ],
            options={
                'verbose_name': 'Metrics',
                'verbose_name_plural': 'Metrics',
            },
        ),
        migrations.CreateModel(
            name='QA_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qa_date', models.DateField(blank=True, default='02/21/2024', max_length=25, null=True, verbose_name='Date')),
                ('qa_time', models.TimeField(blank=True, max_length=25, null=True, verbose_name='Time')),
                ('method', models.CharField(choices=[('Email', 'Email'), ('In Person', 'In Person'), ('Phone', 'Phone'), ('Teams', 'Teams')], max_length=25, null=True, verbose_name='Method')),
                ('related_to', models.CharField(choices=[('Attorney Tone', 'Attorney Tone'), ('Attrition', 'Attrition'), ('Calendar', 'Calendar'), ('Call Time', 'Call Time'), ('DS Benefit', 'DS Benefit'), ('DS Consider', 'DS Consider'), ('DS Not Loan', 'DS Not Loan'), ('EA', 'EA'), ('File Review', 'File Review'), ('Handling Work', 'Handling Work'), ('Identify Self / Comp', 'Identify Self / Comp'), ('Lawsuit', 'Lawsuit'), ('Offer', 'Offer'), ('Recording Disclaimer', 'Recording Disclaimer'), ('Sharpen', 'Sharpen'), ('Understand DS Process', 'Understand DS Process')], max_length=25, null=True, verbose_name='Related To')),
                ('qa_note', models.TextField(blank=True, max_length=255, null=True, verbose_name='Coaching and QA Notes')),
                ('document', models.FileField(blank=True, null=True, upload_to='QA/')),
                ('delivered_by', models.CharField(choices=[], max_length=50, null=True, verbose_name='Author')),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attorneys.employee')),
            ],
            options={
                'verbose_name': 'Coaching and QA',
                'verbose_name_plural': 'Coaching and QA',
            },
        ),
        migrations.CreateModel(
            name='To_Do_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, default='02/21/2024', max_length=25, null=True, verbose_name='Date')),
                ('due_date', models.DateField(blank=True, max_length=25, null=True, verbose_name='Due Date')),
                ('task', models.CharField(blank=True, max_length=255, null=True, verbose_name='Task')),
                ('notes', models.CharField(blank=True, max_length=255, null=True, verbose_name='Notes')),
                ('document', models.FileField(blank=True, null=True, upload_to='Tasks/')),
                ('completed', models.BooleanField(default=False, verbose_name='Completed')),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attorneys.employee')),
            ],
            options={
                'verbose_name': 'To Do List',
                'verbose_name_plural': 'To Do List',
            },
        ),
    ]
