# onboarding.models

from django.conf import settings
from urllib import request

from django.db.models import OneToOneField

from django.contrib.auth.models import User
from django.forms import forms
from datetime import datetime, date
from collections import OrderedDict
from django.db import models
from managers.models import CustomUser
from states.models import State, get_managers
from attorneys.models import Employee

class Onboarding_Detail_Model(models.Model):
    class Meta:
        verbose_name = "Onboarding Detail"
        verbose_name_plural = "Onboarding Detail"

    MANAGER_OPTIONS  = get_managers

    # Administrative Tasks
    employee_id = models.OneToOneField(Employee, on_delete=models.CASCADE)
    add_attorney_more = models.BooleanField("Add additional employee data", default=False)
    pause_job = models.BooleanField("Pause job posting; review and save pending resumes (if needed)", default=False)
    send_onboarding_email = models.BooleanField("Send onboarding email to: ", default=False)
    add_to_spreadsheet = models.BooleanField("Add to spreadsheet", default=False)
    send_spreadsheet = models.BooleanField("Send spreadsheet", default=False)
    save_license = models.BooleanField("Save bar license", default=False)

    # Salaried Positions
    save_offer_letter = models.BooleanField("Save Offer Letter", default=False)
    puzzle_form = models.BooleanField("Complete Puzzle HR Form", default=False)
    include_note = models.BooleanField("Include Note", default=False)
    attach_copy_letter = models.BooleanField("Attach copy of offer letter", default=False)
    employee_referral_form = models.BooleanField("Attach employee referral program form", default=False)

    # Of Counsel Positions
    return_ICA = models.BooleanField("Return fully executed ICAs to attorney", default=False)
    # Huron Employees
    notify_Huron = models.BooleanField("Notify Laura Pina of new attorney start date", default=False)

    # Onboarding and Training Documents
    send_pp_docs = models.BooleanField("Send onboarding documents to attorney", default=False)
    send_software_docs = models.BooleanField("Send software documents to attorney", default=False)

    # Onboarding and Training
    intro_training = models.BooleanField("Schedule firm introduction training", default=False)
    intro_training_date = models.DateField("Intro Training Date", max_length=25, blank=True, null=True)
    salesforce_training = models.BooleanField("Schedule Salesforce and Servicing Training", default=False)
    salesforce_training_date = models.DateField("Salesforce and Servicing Training Date", max_length=25, blank=True, null=True)
    script_training = models.BooleanField("Schedule Individual Script Training", default=False)
    script_training_date = models.DateField("Individual Script Training Date", max_length=25, blank=True, null=True)
    attorney_pp_training = models.BooleanField("Schedule Attorney Policies and Procedures Training", default=False)
    attorney_pp_date = models.DateField("Individual Script Training Date", max_length=25, blank=True, null=True)
    touchbase_meeting = models.BooleanField("Schedule Touch Base Meeting", default=False)
    touchbase_date = models.DateField("Touch Base Date", max_length=25, blank=True, null=True)

    onboarding_completed = models.BooleanField("Save Bar License", default=False)

    def __str__(self):
        return self.employee_id

