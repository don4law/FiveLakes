# managers/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # Custom user with added first name and email as login username
    email = models.EmailField(('email'), unique=True)
    first_name = models.CharField(blank=True, max_length=50, verbose_name='first name')
    middle_name = models.CharField(blank=True, max_length=50, verbose_name='middle name')
    last_name = models.CharField(blank=True, max_length=50, verbose_name='last name')
    initials = models.CharField(blank=True, max_length=50, verbose_name='initials')

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.last_name + ", " + self.first_name + self.middle_name + " ("+ self.email + ")"