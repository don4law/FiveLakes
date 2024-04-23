# attorney.models

from django.conf import settings
from urllib import request

from django.db.models import OneToOneField

from django.contrib.auth.models import User
from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput
from datetime import datetime, date
from collections import OrderedDict
from django.db import models
from managers.models import CustomUser
from django.contrib.auth.models import User
from states.models import State

def get_managers():
    try:
        managers = CustomUser.objects.all().order_by('first_name', 'last_name')
        manager_list = []
        for manager in managers:
            manager_name = manager.first_name + " " + manager.last_name
            manager_tuple = (manager_name, manager_name)
            manager_list.append(manager_tuple)
    except:
        manager_list = []
    return manager_list

def get_manager_options():
    # LIST FOR MANAGER OPTIONS
    states_list = State.objects.all().order_by('manager')
    # Create list of managers
    temp_list = []
    for state in states_list:
        temp_list.append(state.manager)
    manager_list = list(OrderedDict.fromkeys(temp_list))
    # manager_list = []
    # [manager_list.append(manager) for manager in temp_list if manager not in manager_list]
    MANAGER_OPTIONS = []
    for manager in manager_list:
        each_manager = (manager, manager)
        MANAGER_OPTIONS.append(each_manager)
    return MANAGER_OPTIONS

def get_attorneys():
    try:
        attorneys = Employee.objects.all().order_by('first_name', 'last_name')
        attorney_list = []
        for attorney in attorneys:
            attorney_name = attorney.first_name + " " + attorney.last_name
            attorney_tuple = (attorney.employee_id, attorney_name)
            attorney_list.append(attorney_tuple)
    except:
        attorney_list = []
    return attorney_list

def get_active_attorneys():
    # LIST FOR ATTORNEY
    attorneys_list = Employee.objects.filter(is_active=True, onboarding_complete=True).order_by('manager')
    # Create list of attorneys
    ATTORNEY_CHOICES = []
    for attorney in attorneys_list:
        name = attorney.last_name + ', ' + attorney.first_name
        each_attorney = (name, name)
        ATTORNEY_CHOICES.append(each_attorney)
    return ATTORNEY_CHOICES

class Search_Attorneys_Model(models.Model):
    class Meta:
        verbose_name = "Search"
        verbose_name_plural = "Search"

    MANAGER_CHOICES = get_managers()

    states = State.objects.all().order_by('state_abbrev')
    STATE_CHOICES = []
    for state in states:
        each_state = (state.state_abbrev, state.state_abbrev)
        STATE_CHOICES.append(each_state)

    PRIORITY_CHOICES = [
        ('Critical', 'Critical'),
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]

    search_manager = models.CharField("Search by Manager", max_length=25,
        choices = MANAGER_CHOICES, blank=True, null=True)
    search_state = models.CharField("Search by State", max_length=25,
        choices = STATE_CHOICES, blank=True, null=True)
    search_priority = models.CharField("Search by Priority", max_length=25,
        choices = PRIORITY_CHOICES, blank=True, null=True)


class Employee(models.Model):
    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    states = State.objects.order_by('state_abbrev')
    STATE_CHOICES = []
    for state in states:
        each_state = (state.state_abbrev, state.state_abbrev)
        STATE_CHOICES.append(each_state)

    # LIST FOR MANAGER OPTIONS
    states_list = State.objects.all().order_by('manager')
    # Create list of managers
    temp_list = []
    for state in states_list:
        temp_list.append(state.manager)
    manager_list = list(OrderedDict.fromkeys(temp_list))
    # manager_list = []
    # [manager_list.append(manager) for manager in temp_list if manager not in manager_list]
    MANAGER_OPTIONS = []
    for manager in manager_list:
        each_manager = (manager, manager)
        MANAGER_OPTIONS.append(each_manager)

    # Provide possible selections for attorney employment
    # Based on State Profile
    EMPLOYMENT_OPTIONS = [
        ('Full-Time', 'Full-Time'),
        ('Part-Time', 'Part-Time'),
        ('Of Counsel', 'Of Counsel'),
        ('Floater', 'Floater'),
    ]

    SOURCE_OPTIONS = [
        ('Indeed', 'Indeed'),
        ('Linked In', 'Linked In'),
        ('Recruiter', 'Recruiter'),
        ('Employee Referral', 'Employee Referral'),
    ]

    FIRM_OPTIONS = [
        ('Huron Law Group', 'Huron Law Group'),
        ('Five Lakes Law Group', 'Five Lakes Law Group'),
    ]

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]

    STEP_CHOICES = [
        ('New Resume', 'New Resume'),
        ('Interview1', 'Interview1'),
        ('Interview2', 'Interview2'),
        ('Final', 'Final'),
        ('Open File', 'Open File')
    ]

    PRIORITY_CHOICES = [
        ('Critical', 'Critical'),
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]

    employee_id = models.BigAutoField("Employee ID", primary_key=True)
    is_active = models.BooleanField("Is Active", default=True, blank=True, null=True)
    state_abbrev = models.CharField("State", max_length=25,
        choices = STATE_CHOICES, blank=False, null=True)
    position = models.CharField("Position", max_length=25,
        choices = EMPLOYMENT_OPTIONS, blank=True, null=False, default="Full-Time")
    salary = models.CharField("Salary", max_length=10, default = "80,000", blank=False, null=False)
    manager = models.CharField("Manager", max_length=50,
        choices = MANAGER_OPTIONS, blank=True, null=False, default="")
    gender = models.CharField("Gender", max_length=10,
        choices = GENDER_CHOICES, blank=False, null=True)
    first_name = models.CharField("First Name", max_length=25, blank=False, null=False)
    middle_name = models.CharField("Middle Name", max_length=25, blank=True, null=False)
    last_name = models.CharField("Last Name", max_length=25, blank=False, null=False)
    phone = models.CharField("Phone Number", max_length=15, blank=True, null=True)
    email = models.EmailField("Email", max_length=254, blank=True, null=True)
    five_lakes_firm = models.BooleanField("Five Lakes Law Group", default=True)
    huron_firm = models.BooleanField("Huron Law Group", default=False)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    hire_date = models.DateField("Start Date", max_length=255, blank=True, null=True)
    start_date = models.DateField("Start Date", max_length=255, blank=True, null=True)
    onboarding_step = models.CharField("Last Name", max_length=50, blank=True, null=True)
    onboarding_complete = models.BooleanField("Onboarding Complete", default=False)
    priority = models.CharField("Criticality Level", max_length=10,
        choices = PRIORITY_CHOICES, default="Low", blank=False, null=True)
    prev_page = models.CharField("Last Name", max_length=100, blank=True, null=True)


    def __str__(self):
        return self.last_name + ", " + self.first_name + " " + self.middle_name


class Employee_More_Model(models.Model):
    class Meta:
        verbose_name = "Employee's Additional Data"
        verbose_name_plural = "Employees' Additional Data"

    employee_id = models.IntegerField("Employee ID", primary_key=True)
    address1 = models.CharField("Address1", max_length=50, blank=True, null=True)
    address2 = models.CharField("Address2", max_length=50, blank=True, null=True)
    city = models.CharField("City", max_length=50, blank=True, null=True)
    resident_state = models.CharField("State", max_length=5, blank=True, null=True)
    zip = models.CharField("Zip", max_length=25, blank=True, null=True)
    phone2 = models.CharField("Phone Number2", max_length=15, blank=True, null=True)
    phone3 = models.CharField("Phone Number3", max_length=15, blank=True, null=True)
    email2 = models.EmailField("Email2", max_length=254, blank=True, null=True)
    email3 = models.EmailField("Email3", max_length=254, blank=True, null=True)
    state_bar_number = models.CharField("State Bar Number", max_length=25, blank=True, null=True)
    state_bar_document = models.FileField(upload_to='Bar/', blank=True, null=True)
    other_states = models.CharField("Other States", max_length=25, blank=True, null=True)
    signed_offer_letter = models.FileField(upload_to='HR/', blank=True, null=True)
    ICA_agreement = models.FileField(upload_to='HR/', blank=True, null=True)

    def __str__(self):
        return self.employee_id


class QA_Model(models.Model):
    class Meta:
        verbose_name = "Coaching and QA"
        verbose_name_plural = "Coaching and QA"

    MANAGER_OPTIONS  = get_manager_options()

    METHOD_CHOICES = [
        ('Email', 'Email'),
        ('In Person', 'In Person'),
        ('Phone', 'Phone'),
        ('Teams', 'Teams'),
    ]

    RELATED_TO_CHOICES = [
        ('Attorney Tone', 'Attorney Tone'),
        ('Attrition', 'Attrition'),
        ('Calendar', 'Calendar'),
        ('Call Time', 'Call Time'),
        ('DS Benefit', 'DS Benefit'),
        ('DS Consider', 'DS Consider'),
        ('DS Not Loan', 'DS Not Loan'),
        ('EA', 'EA'),
        ('File Review', 'File Review'),
        ('Handling Work', 'Handling Work'),
        ('Identify Self / Comp', 'Identify Self / Comp'),
        ('Lawsuit', 'Lawsuit'),
        ('Offer', 'Offer'),
        ('Recording Disclaimer', 'Recording Disclaimer'),
        ('Sharpen', 'Sharpen'),
        ('Understand DS Process', 'Understand DS Process'),
    ]

    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    qa_date = models.DateField("Date", default=datetime.today().strftime(("%m/%d/%Y")),
               max_length=25, blank=True, null=True)
    qa_time = models.TimeField("Time", max_length=25, blank=True, null=True)
    method = models.CharField("Method", max_length=25, choices = METHOD_CHOICES,
                blank=False, null=True)
    related_to = models.CharField("Related To", max_length=25, choices = RELATED_TO_CHOICES,
                blank=False, null=True)
    qa_note = models.TextField("Coaching and QA Notes",
                blank=True, null=True)
    document = models.FileField(upload_to='QA/', blank=True, null=True)
    delivered_by = models.CharField("Author", max_length=50, choices = MANAGER_OPTIONS,
                blank=False, null=True)

    def __str__(self):
        return self.employee_id, self.method


class HR_Requests_Model(models.Model):
    class Meta:
        verbose_name = "Flex and PTO/UTO Tracking"
        verbose_name_plural = "Flex and PTO/UTO Tracking"

    MANAGER_OPTIONS  = get_manager_options()

    TYPE_CHOICES = [
        ('Flex', 'Flex'),
        ('PTO', 'PTO'),
        ('UTO', 'UTO'),
        ('Other', 'Other'),
    ]

    APPROVAL_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Denied', 'Denied'),
    ]

    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField("Date", default=datetime.today().strftime(("%m/%d/%Y")),
               max_length=25, blank=True, null=True)
    time = models.TimeField("Time", max_length=25, blank=True, null=True)
    request_type = models.CharField("Request Type", max_length=25, choices = TYPE_CHOICES,
                blank=False, null=True)
    request_note = models.CharField("Request Notes", max_length=255,
                blank=True, null=True)
    approval_status = models.CharField("Request Status", default="Pending", max_length=25, choices = APPROVAL_CHOICES,
                blank=False, null=True)
    document = models.FileField(upload_to='HR/', blank=True, null=True)
    reasoning = models.CharField("Decision Reasoning", max_length=255,
                blank=True, null=True)
    decision_manager = models.CharField("Decision Manager", max_length=50, choices = MANAGER_OPTIONS,
                blank=False, null=True)

    def __str__(self):
        return self.employee_id, self.request_type

class Call_Monitoring_Model(models.Model):
    class Meta:
        verbose_name = "Call Monitoring"
        verbose_name_plural = "Call Monitoring"

    MANAGER_OPTIONS  = get_manager_options()

    DISPOSITION_CHOICES = [
        ('None', 'None'),
        ('Left Voicemail', 'Left Voicemail'),
        ('Incomplete Consult', 'Incomplete Consult'),
        ('Positive Consult', 'Positive Consult'),
        ('Credit Concerns', 'Credit Concerns'),
        ('Lawsuit Concerns', 'Lawsuit Concerns'),
        ('Requested Cancellation', 'Requested Cancellation'),
        ('Reconsidering Program', 'Reconsidering Program'),
        ('No Answer', 'No Answer'),
        ('Cancellation Prior to Consult', 'Cancellation Prior to Consult'),
    ]

    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField("Review Date", default=datetime.today().strftime(("%m/%d/%Y")),
               max_length=25, blank=True, null=True)
    call_date = models.DateField("Call Date", max_length=25, blank=True, null=True)
    call_time = models.TimeField("Call Time", max_length=25, blank=True, null=True)
    call_url = models.URLField("Call url (https://app.iz1.sharpen.cx/contactCard/)", blank=True, null=True)
    duration = models.CharField("Duration", max_length=25, blank=True, null=True)
    disposition = models.CharField("Disposition", max_length=50, choices = DISPOSITION_CHOICES,
                blank=False, null=True)
    notes = models.TextField("Call Notes", blank=True, null=True)
    document = models.FileField(upload_to='Calls/', blank=True, null=True)
    reviewer = models.CharField("Reviewer", max_length=50, choices = MANAGER_OPTIONS,
                blank=False, null=True)

    def __str__(self):
        return self.employee_id, self.call_date

class Attorney_Notes_Model(models.Model):
    class Meta:
        verbose_name = "Attorney Notes"
        verbose_name_plural = "Attorney Notes"

    MANAGER_OPTIONS  = get_manager_options()

    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField("Review Date", default=datetime.today().strftime(("%m/%d/%Y")),
               max_length=25, blank=True, null=True)
    from_person = models.CharField("From (Name)", max_length=50, blank=True, null=True)
    notes = models.TextField("Notes / Messages", blank=True, null=True)
    document = models.FileField(upload_to='Notes/', blank=True, null=True)
    follow_up_required = models.BooleanField("Follow-up", default=False)
    follow_up_notes = models.TextField("Follow-Up Notes", blank=True, null=True)
    follow_up_completed = models.BooleanField("Completed", default=False)

    def __str__(self):
        return self.employee_id, self.notes


class To_Do_Model(models.Model):
    class Meta:
        verbose_name = "To Do List"
        verbose_name_plural = "To Do List"

    employee_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateField("Date", max_length=25, blank=True, null=True)
    due_date = models.DateField("Due Date", max_length=25, blank=True, null=True)
    task = models.CharField("Task", max_length=255, blank=True, null=True)
    notes = models.CharField("Notes", max_length=255, blank=True, null=True)
    document = models.FileField(upload_to='Tasks/', blank=True, null=True)
    completed = models.BooleanField("Completed", default=False)

    def __str__(self):
        return self.due_date, self.task


class Metrics_Model(models.Model):
    class Meta:
        verbose_name = "Metrics"
        verbose_name_plural = "Metrics"

    TIMEFRAME_CHOICES = [
        ('Daily', 'Daily'),
        ('Weekly', 'Weekly'),
        ('Monthly', 'Monthly'),
        ('Quarter', 'Quarterly'),
        ('Annual', 'Annual'),
    ]

    METRIC_CHOICES = [
        ('Attrition Rate', 'Attrition Rate'),
        ('Quality Assurance', 'Quality Assurance'),
        ('Bandwidth', 'Bandwidth'),
        ('Call Timeliness', 'Call Timeliness'),
        ('Missing Dispo Codes', 'Missing Dispo Codes'),
        ('Review Completion', 'Review Completion'),
        ('EA Completion', 'EA Completion'),
        ('Pro Se Answer Reviews', 'Pro Se Answer Reviews'),
        ('Other', 'Other'),
    ]

    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField("Metric Date", max_length=25, blank=False, null=True)
    timeframe = models.CharField("Timeframe", max_length=25, choices = TIMEFRAME_CHOICES,
                blank=False, null=True)
    metric = models.CharField("Metric", max_length=25, choices = METRIC_CHOICES,
                blank=False, null=True)
    other_description = models.CharField("Metric", max_length=50, blank=True, null=True)
    value = models.DecimalField("Value", decimal_places=2, max_digits=5, blank=False, null=True, )
    document = models.FileField(upload_to='Metrics/', blank=True, null=True)

    def __str__(self):
        return self.metric, self.value


class Issues_Model(models.Model):
    class Meta:
        verbose_name = "Issues Log"
        verbose_name_plural = "Issues Log"

    ATTORNEY_CHOICES  = get_attorneys()

    employee_id = models.ForeignKey(Employee, max_length=50,
        choices = ATTORNEY_CHOICES, blank=True, null=True, on_delete=models.CASCADE)
    date = models.DateField("Review Date", default=datetime.today().strftime(("%m/%d/%Y")),
               max_length=25, blank=True, null=True)
    from_person = models.CharField("From (Name)", max_length=50, blank=True, null=True)
    issue = models.TextField("Issue Description", blank=True, null=True)
    document = models.FileField(upload_to='Notes/', blank=True, null=True)
    follow_up_required = models.BooleanField("Follow-up", default=False)
    follow_up_notes = models.TextField("Follow-Up Notes", blank=True, null=True)
    follow_up_completed = models.BooleanField("Completed", default=False)

    def __str__(self):
        return self.manager_id, self.employee_id, self.notes
