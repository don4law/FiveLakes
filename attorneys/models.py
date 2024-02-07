# attorney.models

from django.conf import settings
from urllib import request

from django.db.models import OneToOneField

from managers.models import CustomUser
from django.contrib.auth.models import User
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

    employee_id = models.IntegerField("Employee ID", primary_key=True)
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
    start_date = models.DateField("Start Date", max_length=255, blank=False, null=True)
    onboarding_complete = models.BooleanField("Onboarding Complete", default=False)
    priority = models.CharField("Priority", max_length=10,
        choices = PRIORITY_CHOICES, default="Low", blank=False, null=True)

    def __str__(self):
        return self.last_name + ", " + self.first_name + " " + self.middle_name


class QA_Model(models.Model):
    class Meta:
        verbose_name = "Coaching and QA"
        verbose_name_plural = "Coaching and QA"

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

    # LIST FOR ATTORNEY
    attorneys_list = Employee.objects.filter(is_active=True, onboarding_complete=True).order_by('manager')
    # Create list of attorneys
    ATTORNEY_CHOICES = []
    for attorney in attorneys_list:
        name = attorney.last_name + ', ' + attorney.first_name
        each_attorney = (name, name)
        ATTORNEY_CHOICES.append(each_attorney)

    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    qa_date = models.DateField("Date", default=datetime.today().strftime(("%m/%d/%Y")),
               max_length=25, blank=True, null=True)
    qa_time = models.TimeField("Time", max_length=25, blank=True, null=True)
    re_attorney = models.CharField("Attorney", max_length=255, choices = ATTORNEY_CHOICES,
                blank=False, null=True)
    method = models.CharField("Method", max_length=25, choices = METHOD_CHOICES,
                blank=False, null=True)
    related_to = models.CharField("Related To", max_length=25, choices = RELATED_TO_CHOICES,
                blank=False, null=True)
    qa_note = models.TextField("Interviewer #1 Notes", max_length=255,
                blank=True, null=True)
    document = models.FileField(upload_to='QA/', blank=True, null=True)
    delivered_by = models.CharField("Author", max_length=50, choices = MANAGER_OPTIONS,
                blank=False, null=True)

    def __str__(self):
        return self.employee_id

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
