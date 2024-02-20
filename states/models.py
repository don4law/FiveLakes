# states.models

from django.conf import settings
from django.db import models
from managers.models import CustomUser
from django.contrib.auth.models import User
from datetime import datetime


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


class State(models.Model):
    class Meta:
        verbose_name = "State Profile"
        verbose_name_plural = "State Profiles"

    STATE_STATUS = [
        ('Red', 'Red'),
        ('Green', 'Green'),
        ('Other', 'Other'),
        ('Inactive', 'Inactive'),
        ('Not in Network', 'Not in Network'),
    ]

    RECRUITING_STATUS_OPTIONS = [
        ('Recruiting', 'Recruiting'),
        ('Pending', 'Pending'),
        ('Staffed', 'Staffed'),
    ]

    PRIORITY_OPTIONS = [
        ('Critical', 'Critical'),
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
        ('None', 'None'),
    ]

    MANAGERS_CHOICES = get_managers()

    id = models.AutoField(primary_key=True)
    state_abbrev = models.CharField("State Abbreviation", max_length=2, unique=True, null=True, blank=False)
    state_full = models.CharField("State Name", max_length=50, unique=True, null=True, blank=False)
    state_status = models.CharField("Status", max_length=25,
                                    choices=STATE_STATUS, default='Red', blank=True)
    manager = models.CharField("Manager", max_length=50,
                               choices=MANAGERS_CHOICES, null=True, blank=True)
    recruiting_status = models.CharField("Recruiting Status", max_length=25,
                                         choices=RECRUITING_STATUS_OPTIONS, default='Recruiting', blank=True)
    state_priority = models.CharField("Priority", max_length=25,
                                      choices=PRIORITY_OPTIONS, default='Critical', blank=True)
    full_time = models.BooleanField("Full Time", default=True)
    part_time = models.BooleanField("Part Time", default=False)
    of_counsel = models.BooleanField("Of Counsel", default=False)
    floater = models.BooleanField("Floater", default=False)
    # Specific Numbers
    FTE_est = models.IntegerField("Est. FTE", default=0, blank=True)
    full_time_est = models.IntegerField("Est. Full-Time", default=0, blank=True)
    part_time_est = models.IntegerField("Est. Part-Time", default=0, blank=True)
    of_counsel_est = models.IntegerField("Est. Of-Counsel", default=0, blank=True)
    floater_est = models.IntegerField("Estimated Floater", default=0, blank=True)

    def __str__(self):
        return self.state_abbrev
