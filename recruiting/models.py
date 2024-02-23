# recruiting.models

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


class Applicant(models.Model):
    class Meta:
        verbose_name = "Applicant"
        verbose_name_plural = "Applicants"

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

    is_active = models.BooleanField("Is Active", default=True, blank=True, null=True)
    application_date = models.DateField("Application Date", blank=True, null=True)
    state_abbrev = models.CharField("State", max_length=25,
        choices = STATE_CHOICES, blank=False, null=True)
    position = models.CharField("Position", max_length=25,
        choices = EMPLOYMENT_OPTIONS, blank=True, null=False, default="Full-Time")
    salary = models.CharField("Salary", max_length=10, default = "80,000", blank=True, null=True)
    manager = models.CharField("Manager", max_length=50,
        choices = MANAGER_OPTIONS, blank=True, null=False, default="")
    step = models.CharField("Step", max_length=25,
        choices = STEP_CHOICES, default="New Resume", blank=False, null=True)
    source = models.CharField("Recruitment Source", max_length=25,
        choices = SOURCE_OPTIONS, blank=True, null=True)
    employee_referral_name = models.CharField("Referral Employee", max_length=100, blank=True, null=True)
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
    initial_notes = models.TextField("Notes", blank=True, null=True)

    def __str__(self):
        return self.last_name + ", " + self.first_name + " " + self.middle_name


class Interview1_Model(models.Model):
    class Meta:
        verbose_name = "First Interview"
        verbose_name_plural = "First Interview"

    MANAGER_CHOICES = get_managers()

    # manager_name = manager_user.first_name + " " + manager_user.last_name

    applicant_id = models.IntegerField("Applicant id", blank=True, null=True)
    interview1_scheduled = models.BooleanField("First Interview Scheduled", default=False)
    interview1_date = models.DateField("First Interview Date", blank=True, null=True)
    interviewer1_manager = models.CharField("Interviewer", max_length=25,
        choices = MANAGER_CHOICES, blank=True, null=True)
    interview1_notes = models.TextField("Notes", blank=True, null=True)
    interview1_completed = models.BooleanField("First Interview Completed", default=False)
    approved_to_continue = models.BooleanField("Approved to Continue", default=False)
    decline_email_sent = models.BooleanField("Decline Email Sent", default=False)
    retain_in_file = models.BooleanField("Retain in File", default=False)

    def __str__(self):
        return self.interview1_date, self.interview1_completed

class Interview2_Model(models.Model):
    class Meta:
        verbose_name = "Second Interview"
        verbose_name_plural = "Second Interview"

    MANAGER_CHOICES = get_managers()

    # manager_name = manager_user.first_name + " " + manager_user.last_name

    applicant_id = models.IntegerField("Applicant id", blank=True, null=True)
    interview2_scheduled = models.BooleanField("Second Interview Scheduled", default=False)
    interview2_date = models.DateField("Second Interview Date", blank=True, null=True)
    interviewer2_manager1 = models.CharField("Interviewer #1", max_length=25,
        choices = MANAGER_CHOICES, blank=True, null=True)
    interview2_notes1 = models.TextField("Interviewer #1 Notes", blank=True, null=True)
    interviewer2_manager2 = models.CharField("Interviewer # 2", max_length=25,
        choices = MANAGER_CHOICES, blank=True, null=True)
    interview2_notes2 = models.TextField("Interviewer # 2 Notes", blank=True, null=True)
    interview2_completed = models.BooleanField("Second Interview Completed", default=False)
    approved_to_continue = models.BooleanField("Approved to Continue", default=False)
    decline_email_sent = models.BooleanField("Decline Email Sent", default=False)
    retain_in_file = models.BooleanField("Retain in File", default=False)

    def __str__(self):
        return self.interview1_date, self.interview2_completed

class FinalStep_Model(models.Model):
    class Meta:
        verbose_name = "Final Applicant Steps"
        verbose_name_plural = "Final Applicant Steps"

    applicant_id = models.IntegerField("Applicant id", blank=True, null=True)
    applicant_withdrawn = models.BooleanField("Applicant Withdrawal from Consideration", default=False)
    offer_letter_sent_charles = models.BooleanField("Offer Letter Emailed Chief Counsel", default=False)
    offer_letter_sent_applicant = models.BooleanField("Offer Letter Forwarded to Applicant", default=False)
    offer_letter_email_date = models.DateField("Offer Letter Date", blank=True, null=True)
    offer_accepted = models.BooleanField("Offer Accepted and Signed", default=False)
    start_date = models.DateField("Start Date", blank=True, null=True)
    completed = models.BooleanField("Completed and Ready for Onboarding", default=False)

    def __str__(self):
        return self.applicant_id

class Search_Model(models.Model):
    class Meta:
        verbose_name = "Search"
        verbose_name_plural = "Search"

    MANAGER_CHOICES = get_managers()

    states = State.objects.all().order_by('state_abbrev')
    STATE_CHOICES = []
    for state in states:
        each_state = (state.state_abbrev, state.state_abbrev)
        STATE_CHOICES.append(each_state)

    STEP_CHOICES = [
        ('New Resume', 'New Resume'),
        ('Interview1', 'Interview1'),
        ('Interview2', 'Interview2'),
        ('Final', 'Final'),
        ('Open File', 'Open File')
    ]

    search_manager = models.CharField("Search by Manager", max_length=25,
        choices = MANAGER_CHOICES, blank=True, null=True)
    search_state = models.CharField("Search by State", max_length=25,
        choices = STATE_CHOICES, blank=True, null=True)
    search_step = models.CharField("Search by Step", max_length=25,
        choices = STEP_CHOICES, blank=True, null=True)
